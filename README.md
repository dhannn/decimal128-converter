**Analysis of the Implementation of the IEEE-754 Decimal-128 Floating-Point Converter**

The topic, IEEE-754 Decimal-128 floating-point converter, presents a challenge because of its increased precision compared to the usual Decimal32 and Decimal64 taught in class. At first, we needed to take into account to accurately handle numbers with more than 34 digits and the length of the field of a Decimal128 as well. To handle this, we needed to recall the IEEE-754 standard while applying the topic assigned to us.

Moving on to the coding implementation, our group adopted the Model-View-Controller (MVC) architecture, wherein the implementation process was divided into logic and GUI development. Initially, we focused on developing the core logic for the Decimal-128 converter, especially in translating decimal inputs into binary representation, considering rounding methods, and addressing special cases like NaN and infinity. It was a struggle at first to integrate the logic with the application, but the MVC architecture helped us to further incorporate it.

Lastly, testing our implementation presents a significant challenge to our group, specifically in handling edge cases required in the Decimal-128 precision. To fix this, we further documented and analyzed the potential edge cases using pen and paper, which assisted us in tracing it back to unit testing. We were able to recognize the importance of being detail-oriented during the whole implementation of the simulation project.

[Video demo of our project](https://youtu.be/91luqW7JkRM)

In addition, listed below are the test cases for the project:

1. Negative Infinity
   Input: -1 x10 -6177 (Round-TNE)
   &nbsp;&nbsp;&nbsp;&nbsp; Expected Output: 0b1 11110 000000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 (binary)
                    0xf800 0000 0000 0000 0000 0000 0000 0000 (hex)
   &nbsp;&nbsp;&nbsp;&nbsp; Actual Output:![image](https://github.com/dhannn/decimal128-converter/assets/135326621/fcc2fbfd-a1d2-4435-8113-3e79fa0467f1)
          
2. Negative Zero
   Input: -0 x10 6112 (Round-TNE)
   Expected Output: 0b1 01000 100000100000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 (binary)
				            0xa208 0000 0000 0000 0000 0000 0000 0000  (hex)
   Actual Output: ![image](https://github.com/dhannn/decimal128-converter/assets/135326621/62879acc-63b5-4434-893f-e417e2a4f1b0)

3. Normal Negative
   Input: -1112345678901234567890123456789012 x10 -70 (Round-TNE)
   Expected Output: 0b1 01001 011111011010 0010010010 0111000101 1101111000 0010001101 0100110100 1011100111 0000011110 0010100011 1001010110 1111001111 0000010010 (binary)
				            0xa5f6 8927 1778 2353 4b9c 1e28 e56f 3c12  (hex)
   Actual Output:![image](https://github.com/dhannn/decimal128-converter/assets/135326621/4448d5e2-c318-4243-aec5-e00cbb3d404f)

4. Normal Positive
   Input: 1112345678901234567890123456789012 x10 -70 (Round-TNE)
   Expected Output: 0b0 01001 011111011010 0010010010 0111000101 1101111000 0010001101 0100110100 1011100111 0000011110 0010100011 1001010110 1111001111 0000010010 (binary)
				            0x25f6 8927 1778 2353 4b9c 1e28 e56f 3c12  (hex)
   Actual Output: ![image](https://github.com/dhannn/decimal128-converter/assets/135326621/7508b95c-d483-48aa-9a44-381f200ea21a)

5. Positive Infinity
   Input: 1 x10 6112 (Round-TNE)
   Expected Output: 0b0 11110 000000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 (binary)
				            0x7800 0000 0000 0000 0000 0000 0000 0000  (hex)
   Actual Output:![image](https://github.com/dhannn/decimal128-converter/assets/135326621/5244e3f7-b94a-4e33-93ed-2192678beedd)

6. Positive Zero
   Input: 1 x10 6112 (Round-TNE)
   Expected Output: 0b0 01000 100000100000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 0000000000 (binary)
			              0x2208 0000 0000 0000 0000 0000 0000 0000  (hex)
   Actual Output:![image](https://github.com/dhannn/decimal128-converter/assets/135326621/a9aa9142-5c62-4009-b42e-f2d6e5e226e7)

7. Round-down
   Input: 1112345678901234567890123456789012.5 x10 -70 (Round Down)
   Expected Output: 0b0 01001 011111011010 0010010010 0111000101 1101111000 0010001101 0100110100 1011100111 0000011110 0010100011 1001010110 1111001111 0000010010 (binary)
            				0x25f6 8927 1778 2353 4b9c 1e28 e56f 3c12  (hex)
   Actual Output:![image](https://github.com/dhannn/decimal128-converter/assets/135326621/d7e5f198-5077-45da-98b8-d6df46dcdc9b)

8. Round-TNE
   Input: 1112345678901234567890123456789012.5 x10 -70 (Round-TNE)
   Expected Output: 0b0 01001 011111011010 0010010010 0111000101 1101111000 0010001101 0100110100 1011100111 0000011110 0010100011 1001010110 1111001111 0000010010 (binary)
            				0x25f6 8927 1778 2353 4b9c 1e28 e56f 3c12  (hex)
   Actual Output:![image](https://github.com/dhannn/decimal128-converter/assets/135326621/0b027d2b-afa8-4525-a32d-b36f63907931)

9. Round-Up
   Input: 1112345678901234567890123456789012.5 x10 -70 (Round-Up)
   Expected Output: 0b0 01001 011111011010 0010010010 0111000101 1101111000 0010001101 0100110100 1011100111 0000011110 0010100011 1001010110 1111001111 0000010011 (binary)
            				0x25f6 8927 1778 2353 4b9c 1e28 e56f 3c13  (hex)
   Actual Output:![image](https://github.com/dhannn/decimal128-converter/assets/135326621/f4e50423-a94c-4580-9d45-d6a1d3dcfdbb)






   

  

    

