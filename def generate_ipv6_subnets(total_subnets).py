def generate_ipv6_subnets(total_subnets):
    """
    Generate IPv6 subnets within the /16 scope, counting in the specified left-to-right pattern.

    Args:
        total_subnets (int): The total number of subnets to generate.

    Returns:
        list: A list of generated subnets.
    """
    subnets = []
    current = [0, 0, 0, 0]  # Represents the four hexadecimal positions

    for _ in range(total_subnets):
        # Convert the current "nibbles" to a hexadecimal string
        subnet = ''.join(f"{x:x}" for x in current)
        subnets.append(subnet)

        # Increment the counting pattern from left to right
        for i in range(4):
            current[i] += 1
            if current[i] < 16:  # No carry needed
                break
            current[i] = 0  # Reset current nibble and carry to the next
    return subnets


def main():
    print("IPv6 /16 Subnet Generator (Left-to-Right Counting)")
    print("=================================================")
    
    # Ask the user for input
    total_subnets = int(input("Enter the total number of subnets to generate: "))

    # Generate the subnets
    subnets = generate_ipv6_subnets(total_subnets)

    # Display the results
    print("\nGenerated IPv6 /16 Subnets:")
    for subnet in subnets:
        print(subnet)


if __name__ == "__main__":
    main()
