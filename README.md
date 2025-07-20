## 🧬 DNA SNP Checker & Genotype Finder

This is a simple Python program that reads your raw DNA data (in `.csv` format) and helps you check for specific genetic variants (SNPs) and their corresponding genotypes. You can use it to explore traits, health risks, talents, and more — by working with ChatGPT!

---

### ✨ What This Does

* You paste a **list of SNPs** (like `rs4680 rs6265 rs1049353`) into the terminal, either with space seperated or with line seperated
* The program reads your raw DNA file in csv and checks your DNA data for those SNPs and their corresponding genotypes
* It returns a list of genotype results like:

  ```
  rs4680: AA
  rs6265: TT
  rs1049353: CC
  ```

You can then copy those results back to ChatGPT to get a detailed interpretation!

---

### 🔁 How to Use with ChatGPT

1. **Ask ChatGPT**:

   > "I have a raw DNA file and I’m using a Python program to check my genotypes. Could you give me all the relevant SNPs for [insert your trait/question here] (e.g., to find out if I have any genetic risk for heart disease) in a one-line space seperated format, so I can paste them into my program? I will then send you the results as SNPID: genotype pairs (e.g., rs123456: AG) in a single message. After that, I’d like you to analyze my results and tell me more about this condition based on my DNA data."

2. **Run the program from terminal**

3. **Paste the one-line list** into the terminal when prompted by the program.

4. **Copy all of the results** (e.g., `rs4680: AA`) and send it back to ChatGPT.

5. **Get interpretation** like:

   > "This genotype is associated with a higher/lower genetic risk for heart disease based on its influence on cardiovascular function, cholesterol levels, or inflammation markers..."

---

### 📁 What You Need

* Your **DNA file** in `.csv` format (e.g., exported from MyHeritage, 23andMe, or Ancestry)
* Python 3.x installed
* This script (just one file)

---

### 🧠 Why This Exists

This tool bridges the gap between raw DNA data and **genetic self-discovery**. It gives you control over your genetic exploration while making it interactive and educational through ChatGPT.

---

### 💬 Example Use Cases

These are some example questions you can ask ChatGPT to find out more about yourselves:

* Underlying genetical conditions and health information
* ADHD / Autism / Schizophrenia / Depression risk and tendencies
* Diet & metabolism tendencies
* Eye & hair color (to find out whether or not you have any recessive genes (p.s., I found out I have recessive genes for blue eyes and blonde hair!))
* Personality traits
* IQ / EQ / Talents
* Political & philosophical tendencies (just for fun!)

And many more!

---

### 🛡️ Disclaimer

This tool, when used alongside ChatGPT, is not a medical diagnostic tool. However, it can provide a general overview of your genetic traits by quickly batch searching your raw DNA data and identifying the corresponding SNP ID : genotype pairs. For any health-related concerns, please consult a licensed genetic counselor or medical professional.

---
