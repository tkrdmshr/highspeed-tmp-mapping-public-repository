import matplotlib.pyplot as plt
import seaborn as sns

class Scatter():

    def sct_plot(self, x_data, x_axis, y_data, y_axis, title, markersize, figsize):
        fig = plt.figure(figsize = [figsize, figsize])
        plt.tick_params(axis='both', direction = "out", labelsize = 18)
        plt.title(title, fontsize = 25)
        plt.scatter(x_data, y_data, s=markersize, color = "black")
        plt.xlabel(x_axis, fontsize = 24)
        plt.ylabel(y_axis, fontsize = 24)
        plt.rcParams['font.family'] = 'Arial' #全体のフォントを設定
        plt.rcParams['font.size'] = 30 #フォントサイズを設定
        plt.rcParams['lines.linewidth'] = 2 # 線の太さ設定
        return fig
        #plt.savefig("figure/"+title+"")
        #plt.show()


    def sct_plot_overwrite(self, x_data, x_axis, y_data, y_axis, x_data_2, y_data_2, title):
        fig = plt.figure(figsize = [8, 8])
        plt.tick_params(axis='both', direction = "out", labelsize = 18)
        plt.scatter(x_data, y_data, s=100, color = "black" )
        plt.scatter(x_data_2, y_data_2, s=100, color = "red")
        plt.xlabel(x_axis, fontsize = 30)
        plt.ylabel(y_axis, fontsize = 30)
        plt.savefig("figure/"+title+"_overwrite")
        #plt.show()

class Stripplot():

    def stripplot(self, df, title, font, label, marker):
        plt.title(title, fontsize = 25)
        plt.tick_params(axis='both', direction = "in", labelsize = font)
        plt.ylabel(label,  fontsize = font)
        sns.boxplot(data = df,
        boxprops=dict(color = 'black', facecolor='skyblue', linewidth=1),
        medianprops=dict(color='black', linewidth=1),
        whiskerprops=dict(color='black', linewidth=1),
        capprops=dict(color='black', linewidth=1),
        sym = '',
        fliersize = 20)
        sns.swarmplot(data = df, size = marker, linewidth=1, edgecolor='black', color = '1')
        plt.savefig('stripplot_' + title + '_.png')
        #plt.show()
