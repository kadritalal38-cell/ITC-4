
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simulation Data Setup ---
z_catalog = np.array([0.15, 0.5, 1.0, 2.0, 3.5, 5.0, 6.5, 8.0]) 
observed_shear = np.array([0.275, 0.220, 0.165, 0.110, 0.075, 0.048, 0.031, 0.019]) 
observed_density = np.array([4.21, 2.85, 1.62, 0.88, 0.45, 0.22, 0.11, 0.05]) 

# --- 2. Plotting Function (Utilizing Matplotlib) ---
def generate_plots():
    z_dense = np.linspace(0.15, 8.5, 500)
    
    # Plot 1: Lensing Shear
    plt.figure(figsize=(10, 6))
    plt.scatter(z_catalog, observed_shear, color='red', label='Observed')
    plt.title('Lensing Shear Benchmark')
    plt.savefig('itc_lensing_shear_benchmark.png', dpi=300)
    plt.close()

    # Plot 2: Density
    plt.figure(figsize=(10, 6))
    plt.scatter(z_catalog, observed_density, color='red', label='Observed')
    plt.title('Gas Density Profile')
    plt.savefig('itc_gas_density_benchmark.png', dpi=300)
    plt.close()
    print("[+] Plots generated: .png files")

if __name__ == "__main__":
    generate_plots()
