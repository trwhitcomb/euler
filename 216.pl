#!/usr/bin/perl
# Project Euler
# Problem 216
# Primality of the numbers t(n) = 2*n**2 - 1

use Bignum;
use Memoize;

memoize("ExpMod");

# Calculate b^e (mod m)
sub ExpMod
{
    my $b = shift;
    my $e = shift;
    my $m = shift;

    if ($e == 0)
    {
        return 1;
    }
    elsif ($e % 2 == 0)
    {
        return ((ExpMod($b, $e/2, $m) ** 2) % $m);
    }
    else
    {
        return ((ExpMod($b, $e-1, $m) * $b) % $m);
    }
        
}

sub FermatTest
{
    my $n = shift;

    my $a = int(rand($n-2)) + 1;
    if ($a == ExpMod($a, $n, $n))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

sub IsPrime
{
    my $n = shift;

    for ($i=0;$i<5;$i++)
    {
        return 0 if (FermatTest($n) == 0);
    }
    return 1;
}

sub T
{
    my $n = shift;
    return (2 * $n * $n) - 1;
}

my $count = 0;
for ($n=2; $n <= 10000; $n++)
{
    $t = T($n);
    print "\t$n\t$t\n" if ($n % 100 == 0);
    $count += IsPrime($t);
}

print "There were $count Fermat primes found\n";
