# **2. Bias in AI Systems**

## **Core Idea**

Bias in AI means the system produces **systematically unfair or skewed outputs** favoring certain groups over others.
This is not random error—it is **consistent and repeatable unfairness**.

---

## **A. Why Bias Occurs**

### **1. Data Bias (Most Common Cause)**

AI learns from historical data. If data is biased → AI becomes biased.

### **Example**

* Past hiring data: mostly male candidates selected
* AI learns: “male = better candidate”
  → Repeats discrimination

---

### **2. Sampling Bias**

Training data does not represent all groups equally.

### **Example**

* Facial recognition trained mostly on light-skinned faces
  → Performs poorly on darker skin tones

---

### **3. Labeling Bias**

Human annotators introduce subjective bias.

### **Example**

* Labeling “aggressive behavior” more often for certain communities

---

### **4. Algorithmic Bias**

Model design itself may amplify bias.

### **Example**

* Optimization focuses on overall accuracy
  → Ignores minority group performance

---

## **B. Types of Bias**

### **1. Gender Bias**

Example:

> “A CEO is…”
> AI often assumes male

---

### **2. Racial / Ethnic Bias**

Example:

* AI associates certain professions with specific ethnic groups

---

### **3. Socioeconomic Bias**

Example:

* Loan approval AI favors high-income groups

---

### **4. Cultural Bias**

Example:

* AI gives Western-centric answers, ignoring local context

---

## **C. Real-World Case**

### **Hiring AI System**

* Trained on 10 years of company hiring data
* Historical bias: mostly male engineers hired

### **Result**

* AI rejects resumes containing:

  * “Women’s college”
  * Female-related keywords

→ **Bias is automated and scaled**

---

## **D. Impact of Bias**

* Discrimination in hiring, loans, healthcare
* Reinforces social inequality
* Legal and ethical risks
* Loss of trust in AI systems

---

## **E. Bias Amplification (Advanced Insight)**

AI doesn’t just copy bias—it can **amplify it**.

### **Example**

* If dataset has 60% male bias
  → Model may produce 80% male-dominated outputs

Reason:

* Patterns get reinforced during training

---

## **F. Detecting Bias**

### **Methods**

* Compare outputs across groups
* Use fairness metrics:

  * Accuracy per group
  * Error rate differences

### **Example**

* Check:

  * Loan approval rate for men vs women

---

## **G. Mitigation Techniques**

### **1. Data-Level Solutions**

* Use diverse datasets
* Balance representation

---

### **2. Model-Level Solutions**

* Fairness-aware algorithms
* Regularization techniques

---

### **3. Post-Processing**

* Adjust outputs to reduce bias

---

### **4. Human Oversight**

* Human review of critical decisions

---

## **H. Practical Example (End-to-End)**

### **Scenario**

AI resume screening system

### **Problem**

Bias against certain gender

### **Solution Steps**

1. Audit training data
2. Remove biased features
3. Test fairness across groups
4. Add human review layer

---

## **Key Takeaway**

Bias is:

* **Inevitable if unchecked**
* **Dangerous at scale**
* Must be handled at:

  * Data level
  * Model level
  * Deployment level

---

