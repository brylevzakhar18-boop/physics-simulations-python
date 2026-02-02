import numpy as np
import matplotlib.pyplot as plt

def simulate_projectile(v0, angle_deg, g=9.81, dt=0.01):
    """
    Simulate projectile motion without air resistance.
    Returns arrays: t, x, y
    """
    theta = np.deg2rad(angle_deg)

    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    t = [0.0]
    x = [0.0]
    y = [0.0]

    while y[-1] >= 0:
        t.append(t[-1] + dt)
        x.append(x[-1] + vx * dt)
        vy = vy - g * dt
        y.append(y[-1] + vy * dt)

    return t, x, y


# --- main ---
t, x, y = simulate_projectile(v0=20, angle_deg=45)

plt.plot(x, y)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile motion")
plt.grid()
plt.show()
