
import sys

MAX_STEPS = 100000
MAX_INPUT = 10**12

def get_next_collatz(n: int) -> int:
    """Returns the next number in the Collatz sequence."""
    return n // 2 if n % 2 == 0 else 3 * n + 1

def generate_sequence(start_node: int, max_steps: int = MAX_STEPS) -> tuple:
    """
    Generates the Collatz sequence for a given start_node.
    Returns: (sequence_list, max_value, steps, reached_one_flag)
    """
    number=start_node
    sequence=[number]
    max_value=number
    steps=0
    
    while number!=1 and steps<max_steps:
        number=get_next_collatz(number)
        sequence.append(number)
        steps+=1
        
        if number>max_value:
            max_value=number
            
    reached_one=(number==1)
    return sequence,max_value,steps,reached_one

def main():
    print("🎮 The Collatz Conjecture Sequence 🎮")
    print("Also known as the 3n+1 problem\n")
    print("📚 Rules:")
    print("  - If the number is even: divide by 2")
    print("  - If the number is odd: multiply by 3 and add 1")
    print("  - Continue until you reach 1\n")    
    while True:
        try:
            number = int(input("🎯 Enter a positive integer to start: "))
            if number <= 0:
                print("❌ Please enter a positive integer!")
                continue
            if number > MAX_INPUT:
                print(f"⚠️ Input too large! Maximum allowed: {MAX_INPUT:,}")
                continue
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        original_number = number
        sequence, max_value, steps, reached_one = generate_sequence(number, MAX_STEPS)

        print(f"\n🚀 Starting with: {number}")
        print("📊 Sequence:")
        for i,val in enumerate(sequence):
            if i==0:
                print(val,end=" ")
            else:
                print(f" ➡️  {val}", end="")
                if i%10==0:
                    print()



        print("\n\n✅ SEQUENCE COMPLETE!")
        print(f"📍 Starting number: {original_number}")
        print(f"👣 Total steps: {steps}")
        print(f"📏 Sequence length: {len(sequence)}")
        print(f"🏆 Highest number reached: {max_value}")

        if len(sequence) <= 100:
            view_details = input("\n🔍 Would you like to see step-by-step details? (y/n): ").strip().lower()
            if view_details in ['y', 'yes']:
                print("\n📝 Detailed Steps:")
                for i in range(len(sequence) - 1):
                    current = sequence[i]
                    next_num = sequence[i + 1]
                    if current % 2 == 0:
                        print(f"  Step {i + 1}: {current} is even ➡️   {current} ÷ 2 = {next_num}")
                    else:
                        print(f"  Step {i + 1}: {current} is odd ➡️   ({current} × 3) + 1 = {next_num}")

        if reached_one:
            print("\n🎉 The sequence reached 1 as expected!")
        else:
            print(f"\n⚠️ Sequence stopped early after reaching {MAX_STEPS} steps.")
        again = input("\n🔄 Do you want to test another number? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thanks for exploring the Collatz Conjecture! Goodbye!\n")
            break
if __name__=='__main__':
    main()