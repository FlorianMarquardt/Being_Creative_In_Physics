"""
Scientific Discovery: The Black Box Challenge
(plain Python version of Episode2_BlackBoxChallenge.ipynb)

Part of the 'Being creative in physics' lecture series.
Code by Florian Marquardt, 2020. MIT License.

The function blackbox(arg0, arg1, arg2, T=300.0, nsteps=1000) hides a physical system.
It returns the times t and a measurement M(t). Explore! What system is behind this?
What do the parameters mean?

Usage:
    python Episode2_BlackBoxChallenge.py     # runs the examples below, saves the plots as PNG files

or, in your own script in the same folder:
    from Episode2_BlackBoxChallenge import blackbox, solve

To run many experiments at once, pass NumPy arrays (of the same shape) for any of the three
arguments, e.g. arg1=np.linspace(0,1,11). Then M gets an extra last dimension for time:
M[3] is the measurement for the 4th parameter value.

A word of caution about numerics: the black box solves its equations numerically, with a fixed
time step dt = T/nsteps. If the time step is too large, the results can become inaccurate, or
even qualitatively wrong, without any warning. So whenever you see an interesting effect, check
that it does not change when you increase nsteps (for example, double it). Distinguishing real
physics from numerical artefacts is part of the challenge!
"""

import numpy as np
import matplotlib.pyplot as plt # for plotting


# Runge-Kutta solver for a set of differential equations.
# In contrast to many solvers you find in libraries, this one can deal with a solution X(t)
# that is an array of an arbitrary number of dimensions. This will be convenient for batch
# processing etc.

def runge_kutta_step(X,t,rhs,dt):
    """
    One step of the standard Runge-Kutta fourth order. I implemented this here
    to avoid dependency on any external package (you can find nice
    implementations in scipy, for example)
    """
    k1=rhs(X,t)
    k2=rhs(X+0.5*dt*k1,t+0.5*dt)
    k3=rhs(X+0.5*dt*k2,t+0.5*dt)
    k4=rhs(X+dt*k3,t+dt)
    return( (dt/6.)*(k1+2*k2+2*k3+k4) )

def solve(X0,rhs,T,nsteps):
    """
    Solve the differential equation dX/dt=rhs(X,t), for 'nsteps' time steps up to time T,
    with initial value X(t=0)=X0.
    
    Here X0 can have ANY shape as an array, and rhs(X,t) must return the same shape.
    
    This is convenient in case you want to, say, do many trajectories in parallel,
    or reserve one index for the particle number, etc. You do not need to assume
    X to be a 1d array, as you would have to do for some other Runge-Kutta implementations.
    It is also nice to split the positions and velocities, e.g. X[0,:] for the positions
    of all particles, and X[1,:] for the velocities.
    
    Returns: Xs,ts
    
    where the shape of the solution Xs is the same as that of X, except we add another dimension
    at the end, of size 'nsteps'. 'ts' just is a 1d array denoting the time steps for
    the solution.
    
    Plotting the solution may work like this, if X was a 1d array:
    
    plt.plot(ts,Xs[5]) # Note that Xs[5] is the same as Xs[5,:]
    
    ...or like this, if e.g. X[1,:] were all the velocities of all particles:
    
    plt.plot(ts,Xs[1,3]) # plotting velocity of particle number 3: Xs[1,3] is the same as Xs[1,3,:]
    
    (code by Florian Marquardt 2020)
    """
    dt=T/nsteps
    X=np.array(X0,dtype='float')
    Xs=np.zeros(np.shape(X0)+(nsteps,)) # to store all the results: add 'nsteps' dimension
    for j in range(nsteps):
        X+=runge_kutta_step(X,j*dt,rhs,dt)
        Xs[...,j]=X # store result (... means: we don't care how many dimensions there are!)
    ts=dt*(np.array(range(nsteps))+1) # all time points
    return(Xs,ts)


# A black box (Don't look inside! But execute this cell!)
import binascii
exec(binascii.unhexlify(b'0a6465662062625f72687328582c74293a0a20202020676c6f62616c20506172312c506172320a2020202072657475726e28206e702e617272617928205b20585b315d2c202d28312b506172312a6e702e73696e28506172322a7429292a6e702e73696e28585b305d292d302e30312a585b315d205d2029290a64656620626c61636b626f7828617267302c617267312c617267322c543d3330302e302c6e73746570733d31303030293a0a20202020676c6f62616c20506172312c506172320a20202020617267302c617267312c617267323d6e702e62726f6164636173745f617272617973282a5b6e702e6173617272617928612c64747970653d27666c6f6174272920666f72206120696e2028617267302c617267312c61726732295d290a20202020506172313d617267313b20506172323d617267320a2020202058732c74733d736f6c76652858303d5b6e702e7a65726f735f6c696b652861726730292c617267305d2c7268733d62625f7268732c543d542c6e73746570733d6e7374657073290a2020202072657475726e2874732c58735b305d290a').decode('utf-8'))


if __name__ == "__main__":
    # Usage example for 'solve': a simple harmonic oscillator
    def my_rhs(X,t): # definition of a right-hand-side
        # X[0]==position, X[1]==velocity
        return( np.array([ X[1], -X[0] ]) )

    Xs,ts=solve(X0=[0.5,0.0],rhs=my_rhs,T=50.0,nsteps=500)
    plt.figure(dpi=200)
    plt.plot(ts,Xs[0])
    plt.ylabel("position x")
    plt.xlabel("time t")
    plt.savefig("harmonic_oscillator.png")

    # Running the black box
    t,M=blackbox(arg0=1.0,arg1=0.5,arg2=1.0,
                 T=300.0,nsteps=2000)
    plt.figure(dpi=200)
    plt.plot(t,M)
    plt.ylabel("measurement M")
    plt.xlabel("time t")
    plt.savefig("blackbox_example.png")

    print("Saved harmonic_oscillator.png and blackbox_example.png")
    plt.show()
