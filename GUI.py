from tkinter import *
from Statistics import *

main = Tk()
main.title("Statistics")

def ProbabilityPage():

    maingap_1 = Label(main,text = "")
    maingap_1.grid(row = 1, column = 2)

    def BinomialPage():
        Binomial = Tk()
        Binomial.title("Binomial Probability")

        title = Label(Binomial, text = "Binomial Probability Calculator")
        title.grid(row = 0, column = 0, columnspan = 2)

        binomialgap_1 = Label(Binomial, text = "")
        binomialgap_1.grid(row = 1, column = 0)
        
        n_label = Label(Binomial,text = "n")
        n_label.grid(row = 2, column = 0)
        n_entry = Entry(Binomial, bd=5, width = 10)
        n_entry.grid(row = 2, column = 1)

        p_label = Label(Binomial,text = "p")
        p_label.grid(row = 3, column = 0)
        p_entry = Entry(Binomial, bd=5, width = 10)
        p_entry.grid(row = 3, column = 1)

        x_label = Label(Binomial,text = "x")
        x_label.grid(row = 4, column = 0)
        x_entry = Entry(Binomial, bd=5, width = 10)
        x_entry.grid(row = 4, column = 1)

        binomialgap_2 = Label(Binomial,text = "")
        binomialgap_2.grid(row = 5, column = 0)

        def BinomialPDPage():
            n = int(n_entry.get())
            p = float(p_entry.get())
            x = int(x_entry.get())

            prob = BinomialProbability(n,p,x)

            output = Label(Binomial, text = str(prob))
            output.grid(row = 7,column = 0)

            Binomial.mainloop()
        
        BinomialPDButton = Button(Binomial,text = "Binomial PD",command = BinomialPDPage)
        BinomialPDButton.grid(row = 6, column = 0)

        def BinomialCDPage():
            n = int(n_entry.get())
            p = float(p_entry.get())
            x = int(x_entry.get())

            prob = CumulativeBinomial(n,p,x)

            output = Label(Binomial, text = str(prob))
            output.grid(row = 7,column = 1)

            Binomial.mainloop()

        BinomialCDButton = Button(Binomial,text = "Binomial CD",command = BinomialCDPage)
        BinomialCDButton.grid(row = 6, column = 1)

        Binomial.mainloop()

    BinomialButton = Button(main,text = "Binomial Distribution",command = BinomialPage)
    BinomialButton.grid(column = 0,row = 2)

    def PoissonPage():
        Poisson = Tk()
        Poisson.title("Poisson Probability")

        title = Label(Poisson, text = "Poisson Probability Calculator")
        title.grid(row = 0, column = 0, columnspan = 2)

        poissongap_1 = Label(Poisson, text = "")
        poissongap_1.grid(row = 1, column = 0)
        
        lambda_label = Label(Poisson,text = "λ")
        lambda_label.grid(row = 2, column = 0)
        lambda_entry = Entry(Poisson, bd=5, width = 10)
        lambda_entry.grid(row = 2, column = 1)

        x_label = Label(Poisson,text = "x")
        x_label.grid(row = 3, column = 0)
        x_entry = Entry(Poisson, bd=5, width = 10)
        x_entry.grid(row = 3, column = 1)

        gap2 = Label(Poisson,text = "")
        gap2.grid(row = 4, column = 0)

        def PoissonPDPage():
            l = float(lambda_entry.get())
            x = int(x_entry.get())

            prob = PoissonProbability(l,x)

            output = Label(Poisson, text = str(prob))
            output.grid(row = 6,column = 0)

            Poisson.mainloop()
        
        PoissonPDButton = Button(Poisson,text = "Poisson PD",command = PoissonPDPage)
        PoissonPDButton.grid(row = 5, column = 0)

        def PoissonCDPage():
            l = float(lambda_entry.get())
            x = int(x_entry.get())

            prob = CumulativePoisson(l,x)

            output = Label(Poisson, text = str(prob))
            output.grid(row = 6,column = 1)

            Poisson.mainloop()

        PoissonCDButton = Button(Poisson,text = "Poisson CD",command = PoissonCDPage)
        PoissonCDButton.grid(row = 5, column = 1)

        Poisson.mainloop()

    PoissonButton = Button(main,text = "Poisson Distribution",command = PoissonPage)
    PoissonButton.grid(column = 1,row = 2)

    def NormalPage():
        Normal = Tk()
        Normal.title("Normal Probability")

        title = Label(Normal, text = "Normal Probability Calculator")
        title.grid(row = 0, column = 0, columnspan = 2)

        Normalgap_1 = Label(Normal, text = "")
        Normalgap_1.grid(row = 1, column = 0)
        
        mean_label = Label(Normal,text = "μ")
        mean_label.grid(row = 2, column = 0)
        mean_entry = Entry(Normal, bd=5, width = 10)
        mean_entry.grid(row = 2, column = 1)

        stdev_label = Label(Normal,text = "σ")
        stdev_label.grid(row = 3, column = 0)
        stdev_entry = Entry(Normal, bd=5, width = 10)
        stdev_entry.grid(row = 3, column = 1)

        x_label = Label(Normal,text = "x")
        x_label.grid(row = 4, column = 0)
        x_entry = Entry(Normal, bd=5, width = 10)
        x_entry.grid(row = 4, column = 1)

        Normalgap_2 = Label(Normal,text = "")
        Normalgap_2.grid(row = 5, column = 0)

        def NormalCDPage():
            mean = float(mean_entry.get())
            stdev = float(stdev_entry.get())
            x = int(x_entry.get())

            prob = CumulativeNormal(mean,stdev,x)

            output = Label(Normal, text = str(prob))
            output.grid(row = 7,column = 0)

            Normal.mainloop()

        NormalCDButton = Button(Normal,text = "Normal CD",command = NormalCDPage)
        NormalCDButton.grid(row = 6, column = 0)

        Normal.mainloop()

    NormalButton = Button(main,text = "Normal Distribution",command = NormalPage)
    NormalButton.grid(column = 2,row = 2)

    def GeometricPage():
        Geometric = Tk()
        Geometric.title("Geometric Probability")

        title = Label(Geometric, text = "Geometric Probability Calculator")
        title.grid(row = 0, column = 0, columnspan = 2)

        geometricgap_1 = Label(Geometric, text = "")
        geometricgap_1.grid(row = 1, column = 0)
        
        p_label = Label(Geometric,text = "p")
        p_label.grid(row = 2, column = 0)
        p_entry = Entry(Geometric, bd=5, width = 10)
        p_entry.grid(row = 2, column = 1)

        x_label = Label(Geometric,text = "x")
        x_label.grid(row = 3, column = 0)
        x_entry = Entry(Geometric, bd=5, width = 10)
        x_entry.grid(row = 3, column = 1)

        gap2 = Label(Geometric,text = "")
        gap2.grid(row = 4, column = 0)

        def GeometricPDPage():
            p = float(p_entry.get())
            x = int(x_entry.get())

            prob = GeometricProbability(p,x)

            output = Label(Geometric, text = str(prob))
            output.grid(row = 6,column = 0)

            Geometric.mainloop()
        
        GeometricPDButton = Button(Geometric,text = "Geometric PD",command = GeometricPDPage)
        GeometricPDButton.grid(row = 5, column = 0)

        def GeometricCDPage():
            p = float(p_entry.get())
            x = int(x_entry.get())

            prob = CumulativeGeometric(p,x)

            output = Label(Geometric, text = str(prob))
            output.grid(row = 6,column = 1)

            Geometric.mainloop()

        GeometricCDButton = Button(Geometric,text = "Geometric CD",command = GeometricCDPage)
        GeometricCDButton.grid(row = 5, column = 1)

        Geometric.mainloop()

    GeometricButton = Button(main,text = "Geometric Distribution",command = GeometricPage)
    GeometricButton.grid(column = 0,row = 3)

    def NegativeBinomialPage():
        NegativeBinomial = Tk()
        NegativeBinomial.title("Negative Binomial Probability")

        title = Label(NegativeBinomial, text = "Negative Binomial Probability Calculator")
        title.grid(row = 0, column = 0, columnspan = 2)

        NegativeBinomialgap_1 = Label(NegativeBinomial, text = "")
        NegativeBinomialgap_1.grid(row = 1, column = 0)
        
        r_label = Label(NegativeBinomial,text = "r")
        r_label.grid(row = 2, column = 0)
        r_entry = Entry(NegativeBinomial, bd=5, width = 10)
        r_entry.grid(row = 2, column = 1)

        p_label = Label(NegativeBinomial,text = "p")
        p_label.grid(row = 3, column = 0)
        p_entry = Entry(NegativeBinomial, bd=5, width = 10)
        p_entry.grid(row = 3, column = 1)

        x_label = Label(NegativeBinomial,text = "x")
        x_label.grid(row = 4, column = 0)
        x_entry = Entry(NegativeBinomial, bd=5, width = 10)
        x_entry.grid(row = 4, column = 1)

        NegativeBinomialgap_2 = Label(NegativeBinomial,text = "")
        NegativeBinomialgap_2.grid(row = 5, column = 0)

        def NegativeBinomialPDPage():
            r = int(r_entry.get())
            p = float(p_entry.get())
            x = int(x_entry.get())

            prob = NegativeBinomialProbability(r,p,x)

            output = Label(NegativeBinomial, text = str(prob))
            output.grid(row = 7,column = 0)

            NegativeBinomial.mainloop()
        
        NegativeBinomialPDButton = Button(NegativeBinomial,text = "Negative Binomial PD",command = NegativeBinomialPDPage)
        NegativeBinomialPDButton.grid(row = 6, column = 0)

        def NegativeBinomialCDPage():
            r = int(r_entry.get())
            p = float(p_entry.get())
            x = int(x_entry.get())

            prob = CumulativeNegativeBinomial(r,p,x)

            output = Label(NegativeBinomial, text = str(prob))
            output.grid(row = 7,column = 1)

            NegativeBinomial.mainloop()

        NegativeBinomialCDButton = Button(NegativeBinomial,text = "Negative Binomial CD",command = NegativeBinomialCDPage)
        NegativeBinomialCDButton.grid(row = 6, column = 1)

        NegativeBinomial.mainloop()

    NegativeBinomialButton = Button(main,text = "Negative Binomial Distribution",command = NegativeBinomialPage)
    NegativeBinomialButton.grid(column = 1,row = 3)

    def DiscreteUniformPage():
        DiscreteUniform = Tk()
        DiscreteUniform.title("Discrete Uniform Probability")

        title = Label(DiscreteUniform, text = "Discrete Uniform Probability Calculator")
        title.grid(row = 0, column = 0, columnspan = 2)

        DiscreteUniformgap_1 = Label(DiscreteUniform, text = "")
        DiscreteUniformgap_1.grid(row = 1, column = 0)
        
        min_label = Label(DiscreteUniform,text = "min")
        min_label.grid(row = 2, column = 0)
        min_entry = Entry(DiscreteUniform, bd=5, width = 10)
        min_entry.grid(row = 2, column = 1)

        max_label = Label(DiscreteUniform,text = "max")
        max_label.grid(row = 3, column = 0)
        max_entry = Entry(DiscreteUniform, bd=5, width = 10)
        max_entry.grid(row = 3, column = 1)

        x_label = Label(DiscreteUniform,text = "x")
        x_label.grid(row = 4, column = 0)
        x_entry = Entry(DiscreteUniform, bd=5, width = 10)
        x_entry.grid(row = 4, column = 1)

        DiscreteUniformgap_2 = Label(DiscreteUniform,text = "")
        DiscreteUniformgap_2.grid(row = 5, column = 0)

        def DiscreteUniformPDPage():
            min = int(min_entry.get())
            max = float(max_entry.get())

            prob = DiscreteUniformProbability(min,max)

            output = Label(DiscreteUniform, text = str(prob))
            output.grid(row = 7,column = 0)

            DiscreteUniform.mainloop()
        
        DiscreteUniformPDButton = Button(DiscreteUniform,text = "Discrete Uniform PD",command = DiscreteUniformPDPage)
        DiscreteUniformPDButton.grid(row = 6, column = 0)

        def DiscreteUniformCDPage():
            min = int(min_entry.get())
            max = float(max_entry.get())
            x = int(x_entry.get())

            prob = CumulativeDiscreteUniform(min,max,x)

            output = Label(DiscreteUniform, text = str(prob))
            output.grid(row = 7,column = 1)

            DiscreteUniform.mainloop()

        DiscreteUniformCDButton = Button(DiscreteUniform,text = "Discrete Uniform CD",command = DiscreteUniformCDPage)
        DiscreteUniformCDButton.grid(row = 6, column = 1)

        DiscreteUniform.mainloop()

    DiscreteUniformButton = Button(main,text = "Discrete Uniform Distribution",command = DiscreteUniformPage)
    DiscreteUniformButton.grid(column = 2,row = 3)

ProbabilityButton = Button(main,text = "Calculate a Probability", command = ProbabilityPage, height = 2, width = 20)
ProbabilityButton.grid(column = 0, row = 0)

def HypothesisTestPage():
    maingap_1 = Label(main,text = "")
    maingap_1.grid(row = 1, column = 2)

    def BinomialHTPage():
        maingap_2 = Label(main,text="")
        maingap_2.grid(row = 3, column = 0)

        n_label = Label(main,text = "n")
        n_label.grid(row = 4, column = 0)
        n_entry = Entry(main, bd=5, width = 20)
        n_entry.grid(row = 4, column = 1)

        p_label = Label(main,text = "p", width = 20)
        p_label.grid(row = 4, column = 2)
        p_entry = Entry(main, bd=5, width = 20)
        p_entry.grid(row = 4, column = 3)

        maingap_3 = Label(main,text="")
        maingap_3.grid(row = 5, column = 0)

        sig_label = Label(main,text = "α")
        sig_label.grid(row = 6, column = 0)
        sig_entry = Entry(main, bd=5, width = 20)
        sig_entry.grid(row = 6, column = 1)

        testStatistic_label = Label(main,text = "Test Statistic", width = 20)
        testStatistic_label.grid(row = 6, column = 2)
        testStatistic_entry = Entry(main, bd=5, width = 20)
        testStatistic_entry.grid(row = 6, column = 3)

        maingap_4 = Label(main,text="")
        maingap_4.grid(row = 7, column = 0)

        def DoBinomialHT():
            n = int(n_entry.get())
            p = float(p_entry.get())
            sig = float(sig_entry.get())
            testStatistic = int(testStatistic_entry.get())

            prob = CumulativeBinomial(n,p,testStatistic)

            output_1 = Label(main, text = "The probability that the test statistic occured is " + str(prob))
            output_1.grid(row = 9,column = 0, columnspan = 4)

            if prob < sig or prob > 1 - sig:
                output_2 = Label(main, text = "Reject H0, there is sufficient evidence that the assumption is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)
            else:
                output_2 = Label(main, text = "Accept H0, there is insuffienct evidence that the assumptions is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)

        DoBinomialHTButton = Button(main,text = "Do Test", command = DoBinomialHT)
        DoBinomialHTButton.grid(column = 0, row = 8)

    BinomialButton = Button(main,text = "Binomial Distribution",command = BinomialHTPage)
    BinomialButton.grid(column = 0,row = 2)

    def PoissonHTPage():
        maingap_2 = Label(main,text="")
        maingap_2.grid(row = 3, column = 0)

        lambda_label = Label(main,text = "λ")
        lambda_label.grid(row = 4, column = 0)
        lambda_entry = Entry(main, bd=5, width = 20)
        lambda_entry.grid(row = 4, column = 1)

        empty_label = Label(main,text = "", width = 20)
        empty_label.grid(row = 4, column = 2)
        empty_entry = Entry(main, bd=5, width = 20)
        empty_entry.grid(row = 4, column = 3)

        maingap_3 = Label(main,text="")
        maingap_3.grid(row = 5, column = 0)

        sig_label = Label(main,text = "α")
        sig_label.grid(row = 6, column = 0)
        sig_entry = Entry(main, bd=5, width = 20)
        sig_entry.grid(row = 6, column = 1)

        testStatistic_label = Label(main,text = "Test Statistic", width = 20)
        testStatistic_label.grid(row = 6, column = 2)
        testStatistic_entry = Entry(main, bd=5, width = 20)
        testStatistic_entry.grid(row = 6, column = 3)

        maingap_4 = Label(main,text="")
        maingap_4.grid(row = 7, column = 0)

        def DoPoissonHT():
            _lambda = int(lambda_entry.get())
            sig = float(sig_entry.get())
            testStatistic = int(testStatistic_entry.get())

            prob = CumulativePoisson(_lambda,testStatistic)

            output_1 = Label(main, text = "The probability that the test statistic occured is " + str(prob))
            output_1.grid(row = 9,column = 0, columnspan = 4)

            if prob < sig or prob > 1 - sig:
                output_2 = Label(main, text = "Reject H0, there is sufficient evidence that the assumption is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)
            else:
                output_2 = Label(main, text = "Accept H0, there is insuffienct evidence that the assumptions is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)

        DoPoissonHTButton = Button(main,text = "Do Test", command = DoPoissonHT)
        DoPoissonHTButton.grid(column = 0, row = 8)

    PoissonButton = Button(main,text = "Poisson Distribution",command = PoissonHTPage)
    PoissonButton.grid(column = 1,row = 2)

    def NormalHTPage():
        maingap_2 = Label(main,text="")
        maingap_2.grid(row = 3, column = 0)

        mean_label = Label(main,text = "μ")
        mean_label.grid(row = 4, column = 0)
        mean_entry = Entry(main, bd=5, width = 20)
        mean_entry.grid(row = 4, column = 1)

        stdev_label = Label(main,text = "σ", width = 20)
        stdev_label.grid(row = 4, column = 2)
        stdev_entry = Entry(main, bd=5, width = 20)
        stdev_entry.grid(row = 4, column = 3)

        maingap_3 = Label(main,text="")
        maingap_3.grid(row = 5, column = 0)

        sig_label = Label(main,text = "α")
        sig_label.grid(row = 6, column = 0)
        sig_entry = Entry(main, bd=5, width = 20)
        sig_entry.grid(row = 6, column = 1)

        testStatistic_label = Label(main,text = "Test Statistic", width = 20)
        testStatistic_label.grid(row = 6, column = 2)
        testStatistic_entry = Entry(main, bd=5, width = 20)
        testStatistic_entry.grid(row = 6, column = 3)

        maingap_4 = Label(main,text="")
        maingap_4.grid(row = 7, column = 0)

        def DoNormalHT():
            mean = float(mean_entry.get())
            stdev = float(stdev_entry.get())
            sig = float(sig_entry.get())
            testStatistic = float(testStatistic_entry.get())

            prob = CumulativeNormal(mean,stdev,testStatistic)

            output_1 = Label(main, text = "The probability that the test statistic occured is " + str(prob))
            output_1.grid(row = 9,column = 0, columnspan = 4)

            if prob < sig or prob > 1 - sig:
                output_2 = Label(main, text = "Reject H0, there is sufficient evidence that the assumption is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)
            else:
                output_2 = Label(main, text = "Accept H0, there is insuffienct evidence that the assumptions is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)

        DoNormalHTButton = Button(main,text = "Do Test", command = DoNormalHT)
        DoNormalHTButton.grid(column = 0, row = 8)

    NormalButton = Button(main,text = "Normal Distribution",command = NormalHTPage)
    NormalButton.grid(column = 2,row = 2)

    def GeometricHTPage():
        maingap_2 = Label(main,text="")
        maingap_2.grid(row = 3, column = 0)

        p_label = Label(main,text = "p")
        p_label.grid(row = 4, column = 0)
        p_entry = Entry(main, bd=5, width = 20)
        p_entry.grid(row = 4, column = 1)

        empty_label = Label(main,text = "", width = 20)
        empty_label.grid(row = 4, column = 2)
        empty_entry = Entry(main, bd=5, width = 20)
        empty_entry.grid(row = 4, column = 3)

        maingap_3 = Label(main,text="")
        maingap_3.grid(row = 5, column = 0)

        sig_label = Label(main,text = "α")
        sig_label.grid(row = 6, column = 0)
        sig_entry = Entry(main, bd=5, width = 20)
        sig_entry.grid(row = 6, column = 1)

        testStatistic_label = Label(main,text = "Test Statistic", width = 20)
        testStatistic_label.grid(row = 6, column = 2)
        testStatistic_entry = Entry(main, bd=5, width = 20)
        testStatistic_entry.grid(row = 6, column = 3)

        maingap_4 = Label(main,text="")
        maingap_4.grid(row = 7, column = 0)

        def DoGeometricHT():
            p = float(p_entry.get())
            sig = float(sig_entry.get())
            testStatistic = int(testStatistic_entry.get())

            prob = CumulativeGeometric(p,testStatistic)

            output_1 = Label(main, text = "The probability that the test statistic occured is " + str(prob))
            output_1.grid(row = 9,column = 0, columnspan = 4)

            if prob < sig or prob > 1 - sig:
                output_2 = Label(main, text = "Reject H0, there is sufficient evidence that the assumption is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)
            else:
                output_2 = Label(main, text = "Accept H0, there is insuffienct evidence that the assumptions is incorrect")
                output_2.grid(row = 10, column = 0, columnspan = 4)

        DoGeometricHTButton = Button(main,text = "Do Test", command = DoGeometricHT)
        DoGeometricHTButton.grid(column = 0, row = 8)

    GeometricButton = Button(main,text = "Geometric Distribution",command = GeometricHTPage)
    GeometricButton.grid(column = 3,row = 2)

HypothesisTestButton = Button(main,text = "Do a Hypothesis Test", command = HypothesisTestPage, height = 2, width = 20,)
HypothesisTestButton.grid(column = 1, row = 0)

def ChiSquaredTestPage():
    maingap_1 = Label(main,text = "")
    maingap_1.grid(row = 1, column = 0)
    
    insertLabel = Label(main,text = "Enter Next Observed Data:")
    insertLabel.grid(row = 2, column = 0)

    insertEntry = Entry(main, bd = 5, width = 20)
    insertEntry.grid(row = 2, column = 1)

    observed = []
    observedText = "["

    def EnterObserved():
        next = insertEntry.get()
        observed.append(int(next))

        insertEntry.delete(0, len(next))
        
        maingap_2 = Label(main, text = "")
        maingap_2.grid(row = 3, column = 0)

        observedLabel = Label(main, text = "Observed:")
        observedLabel.grid(row = 4, column = 0)

        observedText = "["

        for i in observed:
            observedText += str(i)
            observedText += ","

        observedData = Label(main, text = observedText[0:len(observedText)-1] + "]")
        observedData.grid(row = 4, column = 1, columnspan = 2)

        maingap_3 = Label(main, text = "")
        maingap_3.grid(row = 5, column = 0)

        def DoneObserved():
            addButton.destroy()

            maingap_4 = Label(main, text = "")
            maingap_4.grid(row = 7, column = 0)

            ChooseDistLabel = Label(main, text = "Choose Expected Distribution")
            ChooseDistLabel.grid(row = 8, column = 0, columnspan = 2)

            maingap_5 = Label(main, text = "")
            maingap_5.grid(row = 9, column = 0)

            SignificanceLevelLabel = Label(main, text = "α")
            SignificanceLevelLabel.grid(row = 10, column = 0)

            sig = StringVar(main)

            SignificanceLevelEntry = OptionMenu(main, sig, "0.100", "0.050", "0.025", "0.010", "0.005")
            SignificanceLevelEntry.grid(row = 10, column = 1)

            maingap_6 = Label(main, text = "")
            maingap_6.grid(row = 11, column = 0)

            def BinomialChiSquared():
                significanceLevel = float(sig.get())

                maingap_7 = Label(main, text = "")
                maingap_7.grid(row = 13, column = 0)

                n_label = Label(main,text = "n")
                n_label.grid(row = 14, column = 0)
                n_entry = Entry(main, bd=5, width = 20)
                n_entry.grid(row = 14, column = 1)
                    
                p_label = Label(main,text = "p", width = 20)
                p_label.grid(row = 14, column = 2)
                p_entry = Entry(main, bd=5, width = 20)
                p_entry.grid(row = 14, column = 3)

                maingap_8 = Label(main,text="")
                maingap_8.grid(row = 15, column = 0)

                def DoBinomialChiSquaredTest():
                    N = int(n_entry.get())
                    P_binomial = float(p_entry.get())

                    def generateBinomialExpected(freqTotal,cellsTotal):
                        E = []
                        for i in range(0,cellsTotal-1):
                            prob = BinomialProbability(N,P_binomial,i)
                            nextValue = round(prob*freqTotal,2)
                            E.append(nextValue)
                        lastValue = freqTotal - totalFrequency(E)
                        E.append(round(lastValue,2))
                        return E
                    
                    def chiSquaredTest(O,parametersCalculated):
                        total = totalFrequency(O)
                        cells = len(O)
                        E = generateBinomialExpected(total,cells)

                        if type(E) == str:
                            return E
                        
                        observedFinal = combineCells(O,E)[0]
                        expectedFinal = combineCells(O,E)[1]
                        
                        testStatistic = chiSquaredcalc(observedFinal,expectedFinal)
                        
                        degreesOfFreedom = len(observedFinal) - parametersCalculated - 1
                        CriticalValue = float(data[degreesOfFreedom].split(" ")[SigToColumn(significanceLevel)])
                        
                        ChiSquaredLabel1 = Label(main, text = "The Chi Squared Statistic is:")
                        ChiSquaredLabel1.grid(row = 18, column = 0)
                        ChiSquaredLabel2 = Label(main, text = str(testStatistic))
                        ChiSquaredLabel2.grid(row = 18, column = 1)

                        CriticalValueLabel1 = Label(main, text = "The Critical Value is:")
                        CriticalValueLabel1.grid(row = 19, column = 0)
                        CriticalValueLabel2 = Label(main, text = str(CriticalValue))
                        CriticalValueLabel2.grid(row = 19, column = 1)
                        
                        if testStatistic > CriticalValue:
                            return "Reject H0, the distribution does not fit the data"
                        else:
                            return "Accept H0, the distribution does fit the data"

                    maingap_9 = Label(main, text = "")
                    maingap_9.grid(row = 17, column = 0)

                    output = chiSquaredTest(observed, 0)
                    
                    answer = Label(main, text = output)
                    answer.grid(row = 20, column = 0, columnspan = 2)

                goButton = Button(main, text = "Do Test", command = DoBinomialChiSquaredTest, width = 20)
                goButton.grid(row = 16, column = 0)

            BinomialChiSquaredButton = Button(main, text = "Binomial", command = BinomialChiSquared, width = 20)
            BinomialChiSquaredButton.grid(row = 12, column = 0)

            def PoissonChiSquared():
                significanceLevel = float(sig.get())

                maingap_7 = Label(main, text = "")
                maingap_7.grid(row = 13, column = 0)

                lambda_label = Label(main,text = "λ")
                lambda_label.grid(row = 14, column = 0)
                lambda_entry = Entry(main, bd=5, width = 20)
                lambda_entry.grid(row = 14, column = 1)

                maingap_8 = Label(main,text="")
                maingap_8.grid(row = 15, column = 0)

                def DoPoissonChiSquaredTest():
                    L = int(lambda_entry.get())

                    def generatePoissonExpected(freqTotal,cellsTotal):
                        E = []
                        for i in range(0,cellsTotal-1):
                            prob = PoissonProbability(L,i)
                            nextValue = round(prob*freqTotal,2)
                            E.append(nextValue)
                        lastValue = freqTotal - totalFrequency(E)
                        E.append(round(lastValue,2))
                        return E
                    
                    def chiSquaredTest(O,parametersCalculated):
                        total = totalFrequency(O)
                        cells = len(O)
                        E = generatePoissonExpected(total,cells)

                        if type(E) == str:
                            return E
                        
                        observedFinal = combineCells(O,E)[0]
                        expectedFinal = combineCells(O,E)[1]
                        
                        testStatistic = chiSquaredcalc(observedFinal,expectedFinal)
                        
                        degreesOfFreedom = len(observedFinal) - parametersCalculated - 1
                        CriticalValue = float(data[degreesOfFreedom].split(" ")[SigToColumn(significanceLevel)])
                        
                        ChiSquaredLabel1 = Label(main, text = "The Chi Squared Statistic is:")
                        ChiSquaredLabel1.grid(row = 18, column = 0)
                        ChiSquaredLabel2 = Label(main, text = str(testStatistic))
                        ChiSquaredLabel2.grid(row = 18, column = 1)

                        CriticalValueLabel1 = Label(main, text = "The Critical Value is:")
                        CriticalValueLabel1.grid(row = 19, column = 0)
                        CriticalValueLabel2 = Label(main, text = str(CriticalValue))
                        CriticalValueLabel2.grid(row = 19, column = 1)
                        
                        if testStatistic > CriticalValue:
                            return "Reject H0, the distribution does not fit the data"
                        else:
                            return "Accept H0, the distribution does fit the data"

                    maingap_9 = Label(main, text = "")
                    maingap_9.grid(row = 17, column = 0)

                    output = chiSquaredTest(observed, 0)
                    
                    answer = Label(main, text = output)
                    answer.grid(row = 20, column = 0, columnspan = 2)

                goButton = Button(main, text = "Do Test", command = DoPoissonChiSquaredTest, width = 20)
                goButton.grid(row = 16, column = 0)

            PoissonChiSquaredButton = Button(main, text = "Poisson", command = PoissonChiSquared, width = 20)
            PoissonChiSquaredButton.grid(row = 12, column = 1)

            def GeometricChiSquared():
                significanceLevel = float(sig.get())

                maingap_7 = Label(main, text = "")
                maingap_7.grid(row = 13, column = 0)

                p_label = Label(main,text = "p")
                p_label.grid(row = 14, column = 0)
                p_entry = Entry(main, bd=5, width = 20)
                p_entry.grid(row = 14, column = 1)

                maingap_8 = Label(main,text="")
                maingap_8.grid(row = 15, column = 0)

                def DoGeometricChiSquaredTest():
                    p = float(p_entry.get())

                    def generateGeometricExpected(freqTotal,cellsTotal):
                        E = []
                        for i in range(1,cellsTotal):
                            prob = GeometricProbability(p,i)
                            nextValue = round(prob*freqTotal,2)
                            E.append(nextValue)
                        lastValue = freqTotal - totalFrequency(E)
                        E.append(round(lastValue,2))
                        return E
                    
                    def chiSquaredTest(O,parametersCalculated):
                        total = totalFrequency(O)
                        cells = len(O)
                        E = generateGeometricExpected(total,cells)

                        if type(E) == str:
                            return E
                        
                        observedFinal = combineCells(O,E)[0]
                        expectedFinal = combineCells(O,E)[1]
                        
                        testStatistic = chiSquaredcalc(observedFinal,expectedFinal)
                        
                        degreesOfFreedom = len(observedFinal) - parametersCalculated - 1
                        CriticalValue = float(data[degreesOfFreedom].split(" ")[SigToColumn(significanceLevel)])
                        
                        ChiSquaredLabel1 = Label(main, text = "The Chi Squared Statistic is:")
                        ChiSquaredLabel1.grid(row = 18, column = 0)
                        ChiSquaredLabel2 = Label(main, text = str(testStatistic))
                        ChiSquaredLabel2.grid(row = 18, column = 1)

                        CriticalValueLabel1 = Label(main, text = "The Critical Value is:")
                        CriticalValueLabel1.grid(row = 19, column = 0)
                        CriticalValueLabel2 = Label(main, text = str(CriticalValue))
                        CriticalValueLabel2.grid(row = 19, column = 1)
                        
                        if testStatistic > CriticalValue:
                            return "Reject H0, the distribution does not fit the data"
                        else:
                            return "Accept H0, the distribution does fit the data"

                    maingap_9 = Label(main, text = "")
                    maingap_9.grid(row = 17, column = 0)

                    output = chiSquaredTest(observed, 0)
                    
                    answer = Label(main, text = output)
                    answer.grid(row = 20, column = 0, columnspan = 2)

                goButton = Button(main, text = "Do Test", command = DoGeometricChiSquaredTest, width = 20)
                goButton.grid(row = 16, column = 0)

            GeometricChiSquaredButton = Button(main, text = "Geometric", command = GeometricChiSquared, width = 20)
            GeometricChiSquaredButton.grid(row = 12, column = 2)

            def NegativeBinomialChiSquared():
                significanceLevel = float(sig.get())

                maingap_7 = Label(main, text = "")
                maingap_7.grid(row = 13, column = 0)

                r_label = Label(main,text = "r")
                r_label.grid(row = 14, column = 0)
                r_entry = Entry(main, bd=5, width = 20)
                r_entry.grid(row = 14, column = 1)

                p_label = Label(main,text = "p")
                p_label.grid(row = 14, column = 2)
                p_entry = Entry(main, bd=5, width = 20)
                p_entry.grid(row = 14, column = 3)

                maingap_8 = Label(main,text="")
                maingap_8.grid(row = 15, column = 0)

                def DoNegativeBinomialChiSquaredTest():
                    r = int(r_entry.get())
                    p = float(p_entry.get())

                    def generateNegativeBinomialExpected(freqTotal,cellsTotal):
                        E = []
                        for i in range(r,cellsTotal+r-1):
                            prob = NegativeBinomialProbability(r,p,i)
                            nextValue = round(prob*freqTotal,2)
                            E.append(nextValue)
                        lastValue = freqTotal - totalFrequency(E)
                        E.append(round(lastValue,2))
                        return E
                    
                    def chiSquaredTest(O,parametersCalculated):
                        total = totalFrequency(O)
                        cells = len(O)
                        E = generateNegativeBinomialExpected(total,cells)

                        if type(E) == str:
                            return E
                        
                        observedFinal = combineCells(O,E)[0]
                        expectedFinal = combineCells(O,E)[1]
                        
                        testStatistic = chiSquaredcalc(observedFinal,expectedFinal)
                        
                        degreesOfFreedom = len(observedFinal) - parametersCalculated - 1
                        CriticalValue = float(data[degreesOfFreedom].split(" ")[SigToColumn(significanceLevel)])
                        
                        ChiSquaredLabel1 = Label(main, text = "The Chi Squared Statistic is:")
                        ChiSquaredLabel1.grid(row = 18, column = 0)
                        ChiSquaredLabel2 = Label(main, text = str(testStatistic))
                        ChiSquaredLabel2.grid(row = 18, column = 1)

                        CriticalValueLabel1 = Label(main, text = "The Critical Value is:")
                        CriticalValueLabel1.grid(row = 19, column = 0)
                        CriticalValueLabel2 = Label(main, text = str(CriticalValue))
                        CriticalValueLabel2.grid(row = 19, column = 1)
                        
                        if testStatistic > CriticalValue:
                            return "Reject H0, the distribution does not fit the data"
                        else:
                            return "Accept H0, the distribution does fit the data"

                    maingap_9 = Label(main, text = "")
                    maingap_9.grid(row = 17, column = 0)

                    output = chiSquaredTest(observed, 0)
                    
                    answer = Label(main, text = output)
                    answer.grid(row = 20, column = 0, columnspan = 2)

                goButton = Button(main, text = "Do Test", command = DoNegativeBinomialChiSquaredTest, width = 20)
                goButton.grid(row = 16, column = 0)

            NegativeBinomialChiSquaredButton = Button(main, text = "Negative Binomial", command = NegativeBinomialChiSquared, width = 20)
            NegativeBinomialChiSquaredButton.grid(row = 12, column = 3)

        DoneObservedButton = Button(main, text = "Done", command = DoneObserved, width = 40)
        DoneObservedButton.grid(row = 6, column = 0, columnspan = 2)    

    addButton = Button(main,text = "Add", command = EnterObserved)
    addButton.grid(row = 2, column = 2)

ChiSquaredButton = Button(main, text = "Do a Chi Squared Test", command = ChiSquaredTestPage, height = 2, width = 20)
ChiSquaredButton.grid(column = 2, row = 0)

def DataAnalysisPage():
    maingap_1 = Label(main,text = "")
    maingap_1.grid(row = 1, column = 0)
    
    insertLabel = Label(main,text = "Enter Next Data Point:")
    insertLabel.grid(row = 2, column = 0)

    insertEntry = Entry(main, bd = 5, width = 20)
    insertEntry.grid(row = 2, column = 1)

    data = []
    dataText = "["

    def EnterData():
        next = insertEntry.get()
        data.append(int(next))

        insertEntry.delete(0, len(next))
        
        maingap_2 = Label(main, text = "")
        maingap_2.grid(row = 3, column = 0)

        dataLabel = Label(main, text = "Data:")
        dataLabel.grid(row = 4, column = 0)

        dataText = "["

        for i in data:
            dataText += str(i)
            dataText += ","

        DataOutput = Label(main, text = dataText[0:len(dataText)-1] + "]")
        DataOutput.grid(row = 4, column = 1, columnspan = 2)

        maingap_3 = Label(main, text = "")
        maingap_3.grid(row = 5, column = 0)

        def DoneData():
            addButton.destroy()

            maingap_4 = Label(main, text = "")
            maingap_4.grid(row = 7, column = 0)

            CentralTendencyLabel = Label(main, text = "Measures of Central Tendency:")
            CentralTendencyLabel.grid(row = 8, column = 0)

            maingap_5left = Label(main, text = "")
            maingap_5left.grid(row = 9, column = 0)

            MeanLabel = Label(main, text = "Mean")
            MeanLabel.grid(row = 10, column = 0)

            MeanValue = Label(main, text = str(Mean(data)))
            MeanValue.grid(row = 10, column = 1)

            MedianLabel = Label(main, text = "Median")
            MedianLabel.grid(row = 11, column = 0)

            MedianValue = Label(main, text = str(Median(data)))
            MedianValue.grid(row = 11, column = 1)

            ModeLabel = Label(main, text = "Mode")
            ModeLabel.grid(row = 12, column = 0)

            ModeValue = Label(main, text = str(Mode(data)))
            ModeValue.grid(row = 12, column = 1)

            SpreadLabel = Label(main, text = "Measures of Spread:")
            SpreadLabel.grid(row = 8, column = 2)

            maingap_5right = Label(main, text = "")
            maingap_5right.grid(row = 9, column = 2)

            VarianceLabel = Label(main, text = "Variance")
            VarianceLabel.grid(row = 10, column = 2)

            VarianceValue = Label(main, text = str(Variance(data)))
            VarianceValue.grid(row = 10, column = 3)

            StDevLabel = Label(main, text = "Standard Deviation")
            StDevLabel.grid(row = 11, column = 2)

            StDevValue = Label(main, text = str(StDev(data)))
            StDevValue.grid(row = 11, column = 3)

        DoneDataButton = Button(main, text = "Done", command = DoneData, width = 40)
        DoneDataButton.grid(row = 6, column = 0, columnspan = 2)    

    addButton = Button(main,text = "Add", command = EnterData)
    addButton.grid(row = 2, column = 2)

DataAnalysisButton = Button(main, text = "Data Analysis", command = DataAnalysisPage, height = 2, width = 20)
DataAnalysisButton.grid(column = 3, row = 0)

def RegressionPage():
    maingap_1 = Label(main,text = "")
    maingap_1.grid(row = 1, column = 0)

    InstructionsLabelTop = Label(main, text = "Enter values in order with commas separating them:", justify = CENTER)
    InstructionsLabelTop.grid(row = 2, column = 0, columnspan = 2)  

    maingap_2 = Label(main, text = "")
    maingap_2.grid(row = 3, column = 0)  

    insertXLabel = Label(main,text = "Enter X Values:")
    insertXLabel.grid(row = 4, column = 0)

    insertXEntry = Entry(main, bd = 5, width = 20)
    insertXEntry.grid(row = 4, column = 1)

    insertYLabel = Label(main,text = "Enter Y Values:")
    insertYLabel.grid(row = 5, column = 0)

    insertYEntry = Entry(main, bd = 5, width = 20)
    insertYEntry.grid(row = 5, column = 1)

    maingap_3 = Label(main, text = "")
    maingap_3.grid(row = 6, column = 0)

    def Enter():
        xInput = insertXEntry.get()
        xvalues = xInput.split(",")
        yInput = insertYEntry.get()
        yvalues = yInput.split(",")

        maingap_4 = Label(main, text = "")
        maingap_4.grid(row = 8, column = 0)

        x = []
        y = []

        for i in xvalues:
            x.append(float(i))

        for j in yvalues:
            y.append(float(j))

        if len(x) == len(y):
            a = round(a_value(x,y), 3)
            b = round(b_value(x,y), 3)

            equationOutput = "The equation of the regression line is " + str(a) + " + " + str(b) + "x"

            equationLabel = Label(main, text = equationOutput)
            equationLabel.grid(row = 9, column = 0, columnspan = 2)

            r = PMCC(x,y)

            rOutput = "The correlation coefficient is " + str(r)

            rLabel = Label(main, text = rOutput)
            rLabel.grid(row = 10, column = 0, columnspan = 2)

            sig = StringVar(main)

            SignificanceLevelLabel = Label(main, text = "α")
            SignificanceLevelLabel.grid(row = 9, column = 3)

            SignificanceLevelEntry = OptionMenu(main, sig, "0.100", "0.050", "0.025", "0.010", "0.005")
            SignificanceLevelEntry.grid(row = 9, column = 4)

            def RegressionHT():
                significanceLevel = float(sig.get())
              
                table = open("F:\\Other\\Coding Stuff\\Statistics\\RegressionTable.txt")
                data = table.readlines()

                levels = ["n",0.100,0.050,0.025,0.010,0.005]
                index = levels.index(significanceLevel)

                r = PMCC(x, y)
                n = len(x)

                CriticalValue = float(RegressionData[n-3].split(" ")[index])

                if abs(r)>CriticalValue:
                    result =  "Reject H0, there is sufficient evidence that there is a correlation between the two variables"
                else:
                    result = "Accept H0, there is insufficient evidence that there is a correlation between the two variables"

                maingap_5 = Label(main, text = "")
                maingap_5.grid(row = 11, column = 0)

                CriticalValueLabel = Label(main, text = "The critical value is " + str(CriticalValue), justify = LEFT)
                CriticalValueLabel.grid(row = 12, column = 0, columnspan = 2)

                HypothesisTestLabel = Label(main, text = result, justify = LEFT)
                HypothesisTestLabel.grid(row = 13, column = 0, columnspan = 4)

            RegressionHTButton= Button(main, text = "Hypothesis Test", command = RegressionHT)
            RegressionHTButton.grid(row = 10, column = 3, columnspan = 2)
        else:
            WrongInputLabel = Label(main, text = "Wrong Input")
            WrongInputLabel.grid(row = 9, column = 0)

    EnterButton = Button(main, text = "Enter", command = Enter, width = 20)
    EnterButton.grid(row = 7, column = 0, columnspan = 2)

RegressionButton = Button(main, text = "Regression", command = RegressionPage, height = 2, width = 20)
RegressionButton.grid(row = 0, column = 4)

def Reset():
    for widget in main.winfo_children():
        widget.destroy()

    ProbabilityButton = Button(main,text = "Probability", command = ProbabilityPage, height = 2, width = 20)
    ProbabilityButton.grid(column = 0, row = 0)
    HypothesisTestButton = Button(main,text = "Hypothesis Test", command = HypothesisTestPage, height = 2, width = 20,)
    HypothesisTestButton.grid(column = 1, row = 0)
    ChiSquaredButton = Button(main, text = "Chi Squared Test", command = ChiSquaredTestPage, height = 2, width = 20)
    ChiSquaredButton.grid(column = 2, row = 0)
    DataAnalysisButton = Button(main, text = "Data Analysis", command = DataAnalysisPage, height = 2, width = 20)
    DataAnalysisButton.grid(column = 3, row = 0)
    RegressionButton = Button(main, text = "Regression", command = RegressionPage, height = 2, width = 20)
    RegressionButton.grid(row = 0, column = 4)
    maingap_side = Label(main, text = "", width = 10)
    maingap_side.grid(row = 0, column = 5)
    ResetButton = Button(main, text = "Reset", command = Reset, height = 2, width = 10)
    ResetButton.grid(column = 6, row = 0)
    EndButton = Button(main, text = "Exit", command = End, height = 2, width = 10)
    EndButton.grid(column = 7, row = 0)

maingap_side = Label(main, text = "", width = 10)
maingap_side.grid(row = 0, column = 5)

ResetButton = Button(main, text = "Reset", command = Reset, height = 2, width = 10)
ResetButton.grid(column = 6, row = 0)

def End():
    main.destroy()

EndButton = Button(main, text = "Exit", command = End, height = 2, width = 10)
EndButton.grid(column = 7, row = 0)

main.mainloop() 