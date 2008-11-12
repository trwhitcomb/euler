#!/bin/perl
#
# Project Euler
# Problem 21
# Evaluate the sum of all amicable numbers under 100
use Math::Numbers;

my $MAX_NUM = 10000;

for (my $i = 1; $i < $MAX_NUM; $i++)
{
	$number = Math::Numbers->new($i);
	@divisors = $number->get_divisors;

	$sum_divisors = 0;
	$sum_divisors += $_ foreach @divisors;
	$sum_divisors -= $i;
	
	$divSum[$i] = $sum_divisors;
}

for (my $i = 1; $i < $MAX_NUM; $i++)
{
	# Test for amicable pairs:
	# d(a) = b, d(b) = a, a != b
	$b = $divSum[$i];
	if (($i == $divSum[$b]) and ($i != $b))
	{
		$amicable{$i} += 1;
		$amicable{$b} += 1;
		print "$i\t$b\t$divSum[$b]\n";
	}
}
$sumAmicable += $_ foreach keys %amicable;
print "$sumAmicable\n";
