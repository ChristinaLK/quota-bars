#!/usr/bin/env python3

# import tqdm
from math import floor

quota_dict = {
	"/home/ckoch5": 
		{"Size usage": (15, 20)},
	"/staging/ckoch5": 
		{"Size Usage": (10, 100),
		"Item Usage": (56, 100)}
		}

def print_bar(quotatuple: tuple[float], quant: str, length: int = 40, used_char: str = '#', empty_char: str = '-'):
    usage: float = quotatuple[0]
    total: float = quotatuple[1]
    # Rounding up to nearest int out of 100
    percent_used: int = ceiling((usage / total) * 100)
    # with tqdm.tqdm(total=total,ascii='-#',desc = quant,
    # bar_format=' {desc}: [{bar:40}] {n_fmt}/{total_fmt} GB {percentage:3.0f}%') as static_pbar:
        # static_pbar.update(usage)
    n_used_chars: int = floor(prevent_used * length / 100)
    n_empty_chars: int = length - n_used_chars
    

# bar_format='[{bar}]'
# bar_format=' [{bar}] {n_fmt}/{total_fmt} GB {desc}: {percentage:3.0f}%'
# [default: '{l_bar}{bar}{r_bar}'], where l_bar='{desc}: {percentage:3.0f}%|' and r_bar='| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, ' '{rate_fmt}{postfix}]' Possible vars: l_bar, bar, r_bar, n, n_fmt, total, total_fmt, percentage, elapsed, elapsed_s, ncols, nrows, desc, unit, rate, rate_fmt, rate_noinv, rate_noinv_fmt, rate_inv, rate_inv_fmt, postfix, unit_divisor, remaining, remaining_s, eta. Note that a trailing ": " is automatically removed after {desc} if the latter is empty.

for dirpath in quota_dict: 
    print(dirpath)
    for quantity in quota_dict[dirpath]: 
    	#print(quantity)
    	print_bar(quota_dict[dirpath][quantity], quantity)
    print("     ")
