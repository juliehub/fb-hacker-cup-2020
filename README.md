# fb-hacker-cup-2020
### Problem A: Travel Restrictions
2020 has been a tough year for travelers. Air travel is especially problematic as passengers need to spend long periods in security lines, waiting areas, and crowded cabins where social distancing is difficult to maintain.

To minimize the spread of COVID-19, each airline has decided to reorganize all of their **flight routes in a linear fashion**. The airlines are hoping that by **not making any one country a "hub"**, the spread of the virus will be significantly limited.

An airline's flights normally service `N` countries, running in various directions. Amidst the pandemic, each airline has carefully arranged these `N` countries in a sequence with each assigned a number from `1` to `N`. 

Flights are limited to run **only between pairs of countries that are adjacent** in this sequence, with service in **both directions**. No other flights are available. That is, flights are available from country `i` to country `j` if and only if `|i - j| = 1`.

To make things more complicated, some countries have issued their own restrictions on incoming and outgoing travel. These restrictions are indicated by the characters `I{1..N}` and `O{1..N}`, each of which is either **"N"** or **"Y"**:
- If `I_i = "N"`, then incoming flights to country `i` from any other country are disallowed. Otherwise, if `I_i= "Y"`, they may be allowed.
- If `O_i= "N"`, then outgoing flights from country `i` to any other country are disallowed. Otherwise, if `O_i = "Y"`, they may be allowed.

If a flight between adjacent countries is **disallowed by the restrictions of neither its departure country nor its arrival country**, then it's allowed.

As a consulting data scientist in the airline industry, your job is to determine which trips between the various countries are possible. Let `P_{i,j}= "Y"` if it's possible to travel from country `i` to country `j` via a sequence of `0` or more flights (which may pass through other countries along the way), and `P_{i,j} = "N"` otherwise. Note that `P_{i,i}`  is always `"Y"`. Output this `N∗N` matrix of characters.

**Input**
Input begins with an integer `T`, the **number of airlines**. For each airline, there are **three lines**. The first line contains the integer `N`. The second line contains the length-N string `I_{1..N}`. The third line contains the length-N string `O_{1..N}`.

[Sample Input File](https://github.com/juliehub/fb-hacker-cup-2020/blob/master/travel_restrictions_sample_input.txt)

**Output**
For the `ith` airline, output a line containing "Case #i:" followed by `N` more lines, the `ith` of which contains the length-N string `P_{i,1..N}`.

[Sample Outut File](https://github.com/juliehub/fb-hacker-cup-2020/blob/master/travel_restrictions_sample_output.txt)

**Constraints**
```python
1≤T≤100
2≤N≤50
```
**Explanation of Sample**

In the first case, there are two countries with no restrictions. Therefore, trips between all pairs of countries are possible.

In the second case, there are two countries, and traveling into country 1 is restricted. Since country 2 is the only country adjacent to country 1, the only impossible trip is from country 2 to country 1.

In the third case, there are two countries, both of which restrict inbound travel.

In the fourth case, one may not enter countries 2 or 3, nor exit country 4.

**Validation Test Cases**

[travel_restrictions_validation_input](https://github.com/juliehub/fb-hacker-cup-2020/blob/master/travel_restrictions_validation_input.txt)

[travel_restrictions_validation_output](https://github.com/juliehub/fb-hacker-cup-2020/blob/master/travel_restrictions_validation_output.txt)

**Submission**

[source code](https://github.com/juliehub/fb-hacker-cup-2020/blob/master/fb_ProblemA_Travel_Restrictions.py)

[travel_restrictions_input](https://github.com/juliehub/fb-hacker-cup-2020/blob/master/travel_restrictions_input.txt)

[travel_restrictions_julie_submission_output](https://github.com/juliehub/fb-hacker-cup-2020/blob/master/travel_restrictions_julie_submission_output.txt)
