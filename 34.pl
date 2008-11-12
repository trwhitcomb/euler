#!/bin/perl
#
# Project Euler
# Problem 34
# Find the sum of all numbers which are equal to the sum of their digit 
# factorial functions

use Memoize;

memoize("Factorial");

sub Factorial
{
	my $n = shift;
	if ($n == 0)
	{
		return 1;
	}
	else
	{
		return $n * Factorial($n-1);
	}
}

sub Digits
{
	my $n = shift;
	@digits = split(//, "$n");
	return \@digits;
}

sub SumDigitFactorial
{
	my $n = shift;
	my $sum = 0;

	@digits = @{Digits($n)};
	foreach (@digits)
	{
		$sum += Factorial($_);
	}
	return $sum;
}

my $curiousSum = 0;
my $i = 2;
while ($i++)
{
	if ($i == SumDigitFactorial($i))
	{
		$curiousSum += $i;
		print "$i\t\t$curiousSum\n";
	}
}
