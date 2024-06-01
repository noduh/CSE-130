# 1. Name:
#      Noah Jorgensen
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      Decide if a hotel can be purchased on Pacific Avenue in Monopoly
# 4. What was the hardest part? Be as specific as possible.
#      Removing unnecessary questions. The program I wrote asked questions that didn't need to be asked sometimes
#      This was an easy fix though.
# 5. How long did it take for you to complete the assignment?
#      Maybe an hour or two?


# purchasing variables
price = 0
nc_houses = 0
pc_houses = 0
pa_houses = 0
hotel = 0
total_houses = 0
finished_buying = False
end = False
final_out = ""

# prompts
prompt_pc = "What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
prompt_nc = "What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
prompt_pa = "What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "
prompt_cash = "How much cash do you have to spend? "
prompt_houses = "How many houses are there to purchase? "
prompt_hotels = "How many hotels are there to purchase? "
prompt_color_group = "Do you own all the green properties? (y/n) "

# outputs
out_cash = "You do not have sufficient funds to purchase a hotel at this time."
out_no_houses = "There are not enough houses available for purchase at this time."
out_no_hotels = "There are not enough hotels available for purchase at this time."
out_no_properties = "You cannot purchase a hotel until you own all the properties of a given color group."
out_one_hotel = "You cannot purchase a hotel if the property already has one."
out_swap_nc = "Swap North Carolina's hotel with Pennsylvania's 4 houses."
out_swap_pc = "Swap Pacific's hotel with Pennsylvania's 4 houses."


def out_purchase_a(price, total_houses, nc_houses, pc_houses):
    return f"""This will cost ${price}.
    Purchase 1 hotel and {total_houses} house(s).
    Put 1 hotel on Pennsylvania and return any houses to the bank.
    Put {nc_houses} house(s) on North Carolina.
    Put {pc_houses} house(s) on Pacific."""


def out_purchase_b(price, total_houses, nc_houses):
    return f"""This will cost ${price}.
    Purchase 1 hotel and {total_houses} house(s).
    Put 1 hotel on Pennsylvania and return any houses to the bank.
    Put {nc_houses} house(s) on North Carolina."""


def out_purchase_c(price, total_houses, pc_houses):
    return f"""This will cost ${price}.
    Purchase 1 hotel and {total_houses} house(s).
    Put 1 hotel on Pennsylvania and return any houses to the bank.
    Put {pc_houses} house(s) on Pacific."""


def out_purchase_d(price, total_houses):
    return f"""This will cost ${price}.
    Purchase 1 hotel and {total_houses} house(s).
    Put 1 hotel on Pennsylvania and return any houses to the bank."""


#########
# start #
#########
pc = 0
nc = 0

# Check the user owns all properties
own_all = input(prompt_color_group).lower()
if own_all == "n":
    final_out = out_no_properties
    end = True

# Check if any place has a hotel
if not end:
    pa = int(input(prompt_pa))
    if pa == 5:
        final_out = out_one_hotel
        end = True
    else:
        pc = int(input(prompt_pc))
        if pc == 5:
            final_out = out_swap_pc
            end = True
        else:
            nc = int(input(prompt_nc))
            if nc == 5:
                final_out = out_swap_nc
                end = True

if not end:
    # purchace remaining houses and keep track of where it's purchased
    while not finished_buying:
        if pc == nc and pc == pa:
            if pa < 4:
                remaining = 4 - pa
                pc += remaining
                pa += remaining
                nc += remaining
                pc_houses += remaining
                pa_houses += remaining
                nc_houses += remaining
            else:
                hotel += 1
                finished_buying = True
        elif pc < pa or pc < nc:
            pc += 1
            pc_houses += 1
        elif nc < pc or nc < pa:
            nc += 1
            nc_houses += 1
        elif pa < nc or pa < pc:
            pa += 1
            pa_houses += 1

###################
# decide possible #
###################
if not end:
    price = (nc_houses + pc_houses + pa_houses + hotel) * 200
    cash = int(input(prompt_cash))
    if cash < price:
        final_out = out_cash
        end = True
    else:
        houses_available = 0
        total_houses = nc_houses + pc_houses + pa_houses
        if total_houses != 0:
            houses_available = int(input(prompt_houses))
        if houses_available < total_houses:
            final_out = out_no_houses
            end = True
        else:
            hotels_available = int(input(prompt_hotels))
            if hotels_available < hotel:
                final_out = out_no_hotels
                end = True

#####################
# Make Instructions #
#####################
if not end:
    if nc_houses > 0:
        if pc_houses > 0:
            final_out = out_purchase_a(price, total_houses, nc_houses, pc_houses)
        else:
            final_out = out_purchase_b(price, total_houses, nc_houses)
    else:
        if pc_houses > 0:
            final_out = out_purchase_c(price, total_houses, pc_houses)
        else:
            final_out = out_purchase_d(price, total_houses)

#######
# End #
#######
print(final_out)
