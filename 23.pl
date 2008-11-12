#!/bin/perl
#
# Project Euler
# Problem 23
# Find numbers which cannot be written as the sum of 2 abundant numbers
use Math::Numbers;
use Memoize;

memoize("InArray");

my $MAX_NUM = 28123;

sub InArray
{
	my $testVal = shift;
	our @abundantNumbers;	

	$inArray = 0;
	foreach (@abundantNumbers)
	{
		if ($_ == $testVal) 
		{
			$inArray = 1;
			last;
		}	
	}	
	return $inArray;
}

sub CheckSum
{
	my $n = shift;
	our @abundantNumbers;

	$canBeWritten = 0;
	foreach (@abundantNumbers)
	{
		if (InArray($n - $_))
		{
			$canBeWritten = 1;
			last;
		}
	}
	return $canBeWritten;

}

print "Finding abundant numbers...\n";
for (my $i = 1; $i < $MAX_NUM; $i++)
{
	$number = Math::Numbers->new($i);
	@divisors = $number->get_divisors;

	$sumDivisors = 0;
	$sumDivisors += $_ foreach @divisors;
	$sumDivisors -= $i;
	
	$abundant{$i} += 1 if $sumDivisors > $i;
}
our @abundantNumbers = sort keys %abundant;

print "Checking sums...\n";
$sumVals = 0;
for (my $i = 1; $i < $MAX_NUM; $i++)
{
	if (CheckSum($i) == 0)
	{
		$sumVals += $i;
		print "$i\t$sumVals\n";
	}
}

print "$sumVals\n";
