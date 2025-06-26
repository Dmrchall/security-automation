import subprocess
import argparse
import datetime

def run_nmap(target, ports):
    print(f"[+] Scanning {target} on ports {ports}...\n")
    try:
        result = subprocess.run(
            ["nmap", "-p", ports, "-T4", "-v", target],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("[-] Nmap scan failed:", e)
        return None

def save_report(output, target):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nmap_report_{target}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(output)
    print(f"\n[+] Report saved to {filename}")

if __name__ == "__main__":
     parser = argparse.ArgumentParser(description="Automated Nmap Scanner")
     parser.add_argument("target", help="Target IP or domain")
     parser.add_argument("-p", "--ports", default="1-1000", help="Port range")
     parser.add_argument("-s", "--save", action="store_true", help="Save output to file")
     args = parser.parse_args()

     output = run_nmap(args.target, args.ports)
     if output:
         print(output)
         if args.save:
             save_report(output, args.target.replace('.', '_'))
