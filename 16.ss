(define (digit-sum n)
  (if (= n 0)
      0
      (let ((last-digit (remainder n 10)))
        (+ last-digit
           (digit-sum (quotient n 10))))))

