#!/bin/perl
#
# Project Euler
# Problem 55
# Lychrel numbers

use Bignum;
use Memoize;

memoize("PalSum");
memoize("IsPalindrome");
memoize("Lychrel");

sub IsPalindrome
{
	my $n = shift;
	return ("$n" eq join('', reverse split(//,"$n")));
}

sub PalSum
{
	my $n = shift;
	return $n + join('', reverse split(//,"$n"));
}

sub Lychrel
{
	my $n = shift;
	my $count = shift;

	return -1 if ($count == 50);

	if (IsPalindrome(PalSum($n)))
	{
		return $count;
	}
	else
	{
		return Lychrel(PalSum($n), $count+1);
	}
}

$lychrelCount = 0;
for (my $i = 1; $i < 10000; $i++)
{
	$lychrelCount++ if (Lychrel($i, 0) < 0);
}
print "$lychrelCount\n";
