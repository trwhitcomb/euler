(define (square x)
  (* x x))

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
                    m))
        (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))   
; Compute n^n
(define (exp-self-mod n m)
  (expmod n n m))

; Compute the sum, 1..1000
(define (last-digits last-n digit-mod)
  (if (= 0 last-n)
      0
      (remainder (+ (exp-self-mod last-n digit-mod)
                    (last-digits (- last-n 1) digit-mod))
                 digit-mod)))

(define (last-n-digits last-n num-digits)
  (last-digits last-n (expt 10 num-digits)))

  