print("=" * 50)
print("🔢 PRIME NUMBER GENERATOR & ANALYZER 🔢")
print("=" * 50)
print("📝 Analyze, generate, and factorize prime numbers efficiently.")
import math
while True:
    print("\n" + "—" * 50)
    print("📋 MAIN MENU")
    print("1️⃣  Check if a number is prime")
    print("2️⃣  Generate prime numbers up to N")
    print("3️⃣  Find primes in a range")
    print("4️⃣  Prime factorization")
    print("5️⃣  Find the Nth prime number")
    print("6️⃣  Exit")


    choice = input("\n🎯 Enter your choice (1-6): ").strip()

    if choice == '1':
        print("🔍CHECK IF A NUMBER IS PRIME")        
        try:
            num=int(input("🎯 Enter a number to check: "))
            if num<2:
                print(f"😔 {num} is NOT a prime number. (Primes must be > 1)")
            else:
                is_prime=True
                if num > 2 and num % 2 == 0:
                    is_prime = False
                else:
                    for i in range(3, int(math.sqrt(num)) + 1, 2):
                        if num % i == 0:
                            is_prime = False
                            break
                if is_prime:
                    print(f"✅ {num} is a prime number!")
                else:
                    print(f"😔 {num} is NOT a prime number.")
        except ValueError:
            print("❌ Error: Please enter a valid integer.")

    elif choice == '2':
        print("\n🔢 GENERATE PRIME NUMBERS UP TO N")
        
        try:
            limit = int(input("🎯 Enter the limit (N): "))
            if limit > 10000000:
                print("❌ Error: Limit is too high for this system's memory.")

            if limit < 2:
                print("⚠️ No prime numbers exist below 2.")
            
            else:
                sieve = [True] * (limit + 1)
                sieve[0] = sieve[1] = False
                for p in range(2, int(math.sqrt(limit)) + 1):
                    if sieve[p]:
                        for i in range(p * p, limit + 1, p):
                            sieve[i] = False
                primes = [i for i, is_p in enumerate(sieve) if is_p]
                print(f"✅ Primes up to {limit}: {primes}")
                print(f"📊 Total count: {len(primes)}")

        except ValueError:
            print("❌ Error: Please enter a valid integer!")
    
    elif choice == '3':
        print("\n📍FIND PRIMES IN A RANGE")
        
        try:
            start = int(input("🎯 Enter start of range: "))
            end = int(input("🎯 Enter end of range: "))
            
            if start > end:
                print("❌ Error: Start must be less than or equal to end!")
            elif end < 2:
                print("❌ No prime numbers exist below 2.")
            else:
                current_start = max(2, start)
                sieve = [True] * (end + 1)
                sieve[0] = sieve[1] = False
                for p in range(2, int(math.sqrt(end)) + 1):
                    if sieve[p]:
                        for i in range(p * p, end + 1, p):
                            sieve[i] = False
                primes = [i for i in range(current_start, end + 1) if sieve[i]]
                print(f"✅ Primes between {start} and {end}: {primes}")
        
        except ValueError:
            print("❌ Error:Please enter valid numbers!")
    
    elif choice == '4':
        print("\n🏗️ PRIME FACTORIZATION")

        
        try:
            num = int(input("🎯 Enter a number: "))
            
            if num < 2:
                print(f"⚠️ {num} cannot be factorized into primes.")
            else:
                original_num = num
                factors = []
                divisor = 2
                
                while divisor * divisor <= num:
                    while num % divisor == 0:
                        factors.append(divisor)
                        num = num // divisor
                    divisor += 1
                
                if num > 1:
                    factors.append(num)
                
                result_str = " × ".join(map(str, factors))
                print(f"✅ Factorization: {original_num} = {result_str}")
        
        except ValueError:
            print("❌ Error:Please enter a valid number!")
    
    elif choice == '5':
        print("\n🏆 FIND THE NTH PRIME NUMBER")
        
        try:
            n = int(input("🎯 Enter the value of n: "))
            if n > 1000000:
                print("❌ Error: n is too large. High-range Nth primes require a Segmented Sieve.")

            elif n <= 0:
                print("❌ Please enter a positive number!")
            elif n==1:
                print("The First Prime Number is: 2")
            else:
                limit = 100
                if n < 6:
                    limit = 15 # Smallest limit for tiny N
                else:
                    # Formula: n * (log n + log(log n))
                    log_n = math.log(n)
                    limit = int(n * (log_n + math.log(log_n))) + 10 # Buffer of 10
                
                # Sieve of Eratosthenes (Optimized)
                prime = [True] * (limit + 1)
                prime[0] = prime[1] = False
                p = 2
                while p * p <= limit:
                    if prime[p]:
                        for i in range(p * p, limit + 1, p):
                            prime[i] = False
                    p += 1
                count = 0
                nth_prime = None
                for i in range(2, limit + 1):
                    if prime[i]:
                        count += 1
                        if count == n:
                            nth_prime = i
                            break

                # If our estimate was somehow too low, we handle it (Safety fallback)
                if nth_prime:
                    print(f"🎉 The {n}th prime number is: {nth_prime}")
                else:
                    # This branch is now technically impossible due to the +10 buffer
                    print("❌ Error: Calculation range exceeded.")
        
        except ValueError:
            print("Please enter a valid number!")
    
    elif choice == '6':
        print("\n👋Thank you for using Prime Number Analyzer!")
        break
    
    else:
        print("\n ❌ Invalid choice! Please enter a number between 1 and 6.")
    
    again = input("\n🔄 Return to main menu? (y/n): ").strip().lower()
    if again != 'y':
        print("\n👋 Goodbye!\n")
        break

