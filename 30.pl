#!/usr/bin/perl
#
# Project Euler
# Problem 30
#
# Find the sum of all the numbers that can be written as the sum of 
# fifth powers of their digits

sub PowerDigitSum
{
	my $n = shift;
	my $pow = shift;

	my $sum = 0;
	$sum += ($_ ** $pow) foreach(split(//,"$n"));
	return $sum;
}

my $ii = 2;
my $totalSum = 0;
while ($ii++)
{
	if ($ii == PowerDigitSum($ii, 5))
	{
		$totalSum += $ii;
		print "$totalSum\n";
	}
}

