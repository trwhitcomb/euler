(define (hyper-exp-mod a b mod)
  (if (= b 1)
      a
      (expmod a (hyper-exp-mod a (- b 1) mod) mod)))

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