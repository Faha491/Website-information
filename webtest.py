import subprocess

def get_whois_info():
    website = input("Enter the website address (e.g., example.com): ").strip()

    if not website:
        print("⚠️ Please enter a valid website address!")
        return

    try:
        # Run the WHOIS command
        result = subprocess.run(["whois", website], capture_output=True, text=True, check=True)

        # Print WHOIS information
        print("\n🔍 WHOIS Information:\n")
        print(result.stdout)

    except FileNotFoundError:
        print("❌ WHOIS command not found! Please install WHOIS on your system.")
    except subprocess.CalledProcessError:
        print("⚠️ Failed to fetch WHOIS information. The domain may not exist.")

if __name__ == "__main__":
    get_whois_info()
