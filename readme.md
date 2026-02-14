# Airlines Review Analysis Dashboard

## Overview

This project analyzes airline customer reviews using Power BI, statistical modeling, and sentiment analysis. The objective is to evaluate customer satisfaction, identify key performance drivers, analyze trends over time, and provide strategic recommendations to improve retention and reduce churn on a travel platform.

The dataset includes approximately 12,000 reviews across 422 airlines, rated on a 0–10 scale.

---

## Objectives

- Adjust airline ratings using a Bayesian weighted average model  
- Identify top and bottom performing airlines  
- Analyze year-wise rating trends  
- Determine key drivers influencing overall ratings  
- Perform customer segmentation  
- Conduct sentiment analysis using Azure Language ML  
- Provide strategic recommendations to improve customer retention  

---

## Key Findings

### Overall Performance
- Average Overall Rating: 2.80 / 10  
- Recommendation Rate: 30%  
- Standard Deviation: 2.74  
- Ratings peaked in 2018 (3.38) and declined steadily through 2022  

### Top 5 Airlines (Bayesian Adjusted)
- China Southern – 5.50  
- Cathay Dragon – 4.85  
- Virgin Australia – 4.34  
- Bangkok Airways – 4.23  
- China Airlines – 4.17  

### Bottom 5 Airlines
- Frontier – 1.81  
- Spirit – 1.76  
- Viva Air – 1.72  
- Volaris – 1.70  
- Silver Airways – 1.69  

### Driver Analysis
Strongest correlation with overall rating:
- Ground Service  
- Value for Money  

Moderate impact:
- Cabin Staff  
- Seat Comfort  

Lower impact:
- WiFi  
- In-Flight Entertainment  

### Sentiment Distribution
- Negative: 44.22%  
- Neutral: 33.07%  
- Positive: 22.69%  

Customer sentiment is predominantly negative and aligns with low overall ratings.

---

## Methodology

- Bayesian weighted rating adjustment to account for review volume imbalance  
- Correlation heatmap to identify rating drivers  
- Time-series trend analysis  
- Segmentation by traveler type and seat class  
- Sentiment classification using Azure Language ML  

---

## Strategic Recommendations

- Implement intelligent ranking beyond lowest price  
- Introduce value-based scoring metrics  
- Increase transparency in airline performance indicators  
- Add expectation management signals for low-rated options  
- Develop churn prediction and retention triggers  
- Establish closed-loop feedback systems  

---

## Tools Used

- Power BI  
- DAX  
- Python  
- Azure Language ML  

---
