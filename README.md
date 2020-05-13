# Resource Allocator

## Problem statement
The following are the available machines along with their respective capacities.
<ul>
<li>Large – 10 units
<li>XLarge – 20 units 
<li>2XLarge – 40 units
<li>4XLarge – 80 units
<li>8XLarge – 160 units
<li>10XLarge – 320 units
</ul>

These machines are located all over the world and depending on which part of the world they are located in, they have associated costs based on the number of hours they are utilised. Below are the per hour costs

 	            New York	India	China
    Large	    $ 120	    $ 140	$ 110
    XLarge	    $ 230	 	        $ 200
    2XLarge	    $ 450	    $ 413	 
    4XLarge	    $ 774	    $ 890	$ 670
    8XLarge	    $ 1400	    $ 1300	$ 1180
    10XLarge    $ 2820	    $ 2970	 
 
Write an optimized resource allocator program that can be used for cost planning. The program takes the below 2 inputs:

<b>Hours</b>: No of hours the machine is required to run

<b>Capacity</b>: No of units are required (Will always be multiple of 10)

Based on these inputs, the program should optimally allocate the resources such that the cost of the capacity required is minimum. 

Calculate this for every region and show them as the below example.

<b>Sample Input</b>: 

    Capacity of 1150 units for 1 Hour

<b>Expected Output</b>:

    {

    “Output”: [

        {

        “region”: “New York”,

        “total_cost”: “$10150”,

        “machines”: [

            (8XLarge, 7),

            (XLarge, 1),

            (Large, 1)

        ]

        },

        {

        “region”: “India”,

        “total_cost”: “$9520”,

        “machines”: [

            (8XLarge, 7),

            (Large, 3)

        ] 

        },

        {

        “region”: “China”,

        “total_cost”: “$8580”,

        “machines”: [

            (8XLarge, 7),

            (XLarge, 1),

            (Large, 1)

        ] 

        },

    ]

    }

