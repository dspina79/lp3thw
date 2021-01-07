# Truth Table Builder

def write_blank(): 
    """Writes a blank line."""
    print("\n")

def write_two_elements(conditional_statement):
    """Outputs a truth table header with two variables."""
    print(f"\tp\tq\t{conditional_statement}")

def write_and_entry(p,q):
    """Outputs a logical 'and' truth table line."""
    print(f"\t{p}\t{q}\t{p and q}")

def write_or_entry(p,q):
    """Outputs a logical 'or' truth table line."""
    print(f"\t{p}\t{q}\t{p or q}")

def write_conditional_if_entry(p,q):
    """Outputs a logical 'if' truth table line."""
    result = conditional_logic_check(p, q)
    print(f"\t{p}\t{q}\t{result}")

def build_and_table():
    """Generates a logical 'and' truth table."""
    ps = [True, True, False, False]
    qs = [True, False, True, False]
    write_two_elements('p AND q')
    for i in range(4):
        write_and_entry(ps[i], qs[i])
    write_blank()

def build_or_table():
    """Generates a logical 'or' truth table."""
    ps = [True, True, False, False]
    qs = [True, False, True, False]
    write_two_elements('p OR q')
    for i in range(4):
        write_or_entry(ps[i], qs[i])
    write_blank()

def build_logical_if_table():
    """Generates a logical 'if' conditional truth table output."""
    ps = [True, True, False, False]
    qs = [True, False, True, False]
    write_two_elements('p -> q')
    for i in range(4):
        write_conditional_if_entry(ps[i], qs[i])
    write_blank()

def conditional_logic_check(p, q):
    """Performs a conditional (logical) if (p -> q) check."""
    if p and (not q):
        return False
    else:
        return True

build_and_table()
build_or_table()
build_logical_if_table()