# Aim of this program is to simulate the dynamics of a single pendulum

# libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# constants
g = 9.81            # gravitational constant
l = 1               # length of cord the mass is attached to
theta = np.pi / 4   # initial angle mass is displaced by

# ODE - theta and time are dependent/independent vars. respectively
# let z = d(theta)/dt, reduce 2nd order ODE to 1st order


def model(Y, t):  # Y = [theta(t), d(theta)/dt]

    return [Y[1], -(g / l)*np.sin(Y[0])]


def main():
    t = np.linspace(0, 2*np.pi, 1000)
    sol = odeint(model, [theta, 0], t)  # [theta(t = 0) = π/4, (d(theta)/dt)(t=0) = 0]

    # theta against time, calculated by solving the ODE
    plt.plot(t, sol[:, 0])
    plt.title("Theta against time")
    plt.show()

    # acceleration against time (a = -g*sin(theta))
    plt.plot(t, -g * np.sin(sol[:, 0]))
    plt.title("Acceleration against time")
    plt.show()

    # velocity against time (v = l * d(theta)/dt)
    plt.plot(t, l * sol[:, 1])
    plt.title("Velocity against time")
    plt.show()

    # arc length of pendulum against time (s = l * theta)
    plt.plot(t, l * sol[:, 0])
    plt.title("Arc length against time")
    plt.show()


if __name__ == "__main__":
    main()
