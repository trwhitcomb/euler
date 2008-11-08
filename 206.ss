; Project Euler
; Problem 206

(define (find-square n)
  (let ((n-squared (square n)))
    (cond ((= 0 (remainder n 100000))
           (display n)
           (newline)))
    (if (and (= 0 (nth-digit n-squared 1))
             (= 9 (nth-digit n-squared 3))
             (= 8 (nth-digit n-squared 5))
             (= 7 (nth-digit n-squared 7))
             (= 6 (nth-digit n-squared 9))
             (= 5 (nth-digit n-squared 11))
             (= 4 (nth-digit n-squared 13))
             (= 3 (nth-digit n-squared 15))
             (= 2 (nth-digit n-squared 17))
             (= 1 (nth-digit n-squared 19)))
        n-squared
        (find-square (+ 1 n)))))
(define (square x)
  (* x x))

; Get the nth digit of a number
; 54321 2 => 2
(define (nth-digit number n)
  (let ((En-1 (expt 10 (- n 1))))
    (/ (- (remainder number (* En-1 10)) 
          (remainder number En-1))
       En-1)))


(find-square 1010101011)




