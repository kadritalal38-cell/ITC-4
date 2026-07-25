
import numpy as np
import matplotlib.pyplot as plt

# --- ITC Matrix Visual Plotting Engine ---
# Ingest Data
z_data = np.array([0.15, 0.5, 1.0, 2.0, 3.5, 5.0, 6.5, 8.0])
shear = np.array([0.275, 0.220, 0.165, 0.110, 0.075, 0.048, 0.031, 0.019])
density = np.array([4.21, 2.85, 1.62, 0.88, 0.45, 0.22, 0.11, 0.05])

# Modeling Functions
def get_physics(z):
    itc_s = 0.28 / (1.0 + 1.8 * z)
    itc_d = 4.5 / (1.0 + 1.5 * z)
    lcdm_s = 0.28 * np.exp(-z / 2.0)
    lcdm_d = 4.5 * (1.0 + (z / 0.5)**2)**(-0.75)
    return itc_s, itc_d, lcdm_s, lcdm_d

# Plotting
def create_plots():
    z_range = np.linspace(0.15, 8.5, 500)
    itc_s, itc_d, lcdm_s, lcdm_d = get_physics(z_range)
    
    # Plot 1: Shear
    plt.figure()
    plt.scatter(z_data, shear, color='red', label='JWST Data')
    plt.plot(z_range, itc_s, 'b-', label='ITC Model')
    plt.plot(z_range, lcdm_s, 'k--', label='$\Lambda$CDM')
    plt.xlabel('z'); plt.ylabel('Shear'); plt.legend(); plt.grid(True)
    plt.savefig('itc_lensing_shear.png')
    
    # Plot 2: Density
    plt.figure()
    plt.scatter(z_data, density, color='red', label='Chandra Data')
    plt.plot(z_range, itc_d, 'b-', label='ITC Model')
    plt.plot(z_range, lcdm_d, 'k--', label='$\Lambda$CDM')
    plt.xlabel('z'); plt.ylabel('Density'); plt.legend(); plt.grid(True)
    plt.savefig('itc_gas_density.png')
    print("Plots generated.")

if __name__ == "__main__":
    create_plots()
