VITyarthi Mess Comparison Tool

1. Problem Statement

College students frequently struggle to make informed, efficient choices regarding daily dining due to the lack of a centralized system for comparing available food options. Decisions are often based on unreliable word-of-mouth recommendations, leading to dissatisfaction, wasted time, and suboptimal expense management.

Specifically, the problem is the absence of an instantaneous, objective, and comparative tool that allows students to assess the price-to-quality ratio of specific dishes across multiple campus messes simultaneously. This leads to:

Financial Inefficiency: Students miss opportunities to choose the cheapest mess for a particular dish.

Quality Uncertainty: Students cannot easily identify which mess offers the best-rated version of their desired food item.

2. Scope of the Project

The scope of the VITyarthi Mess Comparison Tool is narrowly focused on providing command-line data analysis based on pre-existing, static input files.

In Scope:

Loading and parsing data from two distinct, mandatory Microsoft Excel files (Price.xlsx and Rating.xlsx).

Performing basic data manipulation and indexing using the pandas library.

Allowing the user to select between a Price Comparison (minimum value) or a Rating Comparison (maximum value).

Generating clear, printed output to the console for every dish listed in the input files.

Identifying and reporting the best (cheapest/highest-rated) mess for each dish.

Out of Scope (Current Version):

Web/Mobile application development or a graphical user interface (GUI).

Integration with a live database or real-time data fetching.

User-submitted reviews or ratings.

Error handling for corrupted or incorrectly formatted input files.

3. Target Users

The primary users of this project are individuals directly involved in college dining decisions:

College Students:	Saving money and ensuring quality by finding the cheapest or best-rated food item instantly.

Budget-Conscious Students:	Prioritizing the Price Comparison feature to minimize daily food expenses.

Quality-Focused Students:	Prioritizing the Rating Comparison feature for the best dining experience.

College Administrators (Secondary):	Using the consolidated data to identify which messes are excelling or lagging
                                    in pricing and quality metrics.

4. High-Level Features

Input Management:	Reads and structures price and rating data from two separate Excel sheets (Price.xlsx and Rating.xlsx) 
                  using pandas DataFrames.

Mode Selection:	Provides an interactive command-line prompt for the user to choose between the two 
                primary comparison modes: Price (1) or Rating (2).

Cost Optimization Logic:	For every dish, automatically executes a comparison to identify the column (Mess Name) 
                          with the minimum price (.idxmin()).

Quality Maximization Logic:	For every dish, automatically executes a comparison to identify the column (Mess Name)
                            with the maximum rating (.idxmax()).

Formatted Output:	Presents the comparison result for each dish in a clear, easy-to-read, single-line format on the console.
