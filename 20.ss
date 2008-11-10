; Project Euler
; Problem 20
;
; n! means n * (n-1) * ... * 3 * 2 * 1
; Find the sum of the digits in the number 100!

(define (sum-of-digits n)
  (if (< n 10)
      n
      (+ (remainder n 10)
         (sum-of-digits (quotient n 10)))))

(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))

(sum-of-digits (factorial 100))


