#!/usr/bin/perl
#

use bignum;
use Memoize;

memoize('DigitSum');

sub DigitSum
{
    my $number = shift;
    my @nums   = split //, "$number";

    my $total = 0;
    map {$total += $_} @nums;
    return $total;
}

$maxval = 0;
for ($a = 1; $a <= 100; $a++)
{
    print "A = $a\n";
    for ($b = 1; $b <= 100; $b++)
    {
        $digitSum = DigitSum($a**$b);
        $maxval = ($digitSum > $maxval) ? $digitSum : $maxval;
    }
}

print "Maximum value is $maxval\n";

