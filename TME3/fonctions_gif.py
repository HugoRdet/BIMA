with imageio.get_writer('exo1_8.gif', mode='I') as writer:
    for i in range(0,256,1):
        image = imageio.imread('./img/images_gif_1/exo1_'+str(i)+'.png')
        writer.append_data(image)

for i in range(1,256,1):
    os.remove('./img/images_gif_1/exo1_'+str(i)+'.png') 

nb_images=5
tmp_arr=np.linspace(1,16,nb_images)

#VARIATION FREQUENCE
for i in range(0,tmp_arr.shape[0],1):

    fig = plt.figure(figsize=plt.figaspect(0.5))

    I2=sinusoid2d(A=1,theta=45,T0=64,Te=1/(tmp_arr[i]*fm),size=512)
    ax = fig.add_subplot(1, 3, 1)
    ax.imshow(I2,cmap="gray")
    ax.set_title('sampling frequency = '+str(np.round(tmp_arr[i]*fm,2))+' Hz fm = '+str(np.round(fm,2))+' Hz')
    ax = fig.add_subplot(1, 3, 2, projection='3d')
    X,Y = np.meshgrid(range(I2.shape[1]), range(I2.shape[0]))

    ax.plot_surface(X, Y, I2, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax = fig.add_subplot(1, 3, 3, projection='3d')
    ax.plot_surface(X, Y, np.abs(np.fft.fftshift(np.fft.fft2(I2))), cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.savefig('./img/images_gif_1/exo1_'+str(i)+'.png')
    plt.close()

#variation PERIODE

nb_images=256
tmp_arru=np.linspace(10,200,nb_images)

for i in range(0,tmp_arru.shape[0],1):
    fig = plt.figure(figsize=plt.figaspect(0.5))

    I2=sinusoid2d(A=1,theta=45,T0=tmp_arru[i],Te=1/(64*fm),size=128)
    ax = fig.add_subplot(1, 3, 1)
    ax.imshow(I2,cmap="gray")
    ax.set_title("T0 : "+str(tmp_arru[i]))
    ax = fig.add_subplot(1, 3, 2, projection='3d')
    X,Y = np.meshgrid(range(I2.shape[1]), range(I2.shape[0]))

    ax.plot_surface(X, Y, I2, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    ax = fig.add_subplot(1, 3, 3)
    ax.imshow(np.log(1+np.abs(np.fft.fftshift(np.fft.fft2(I2)))),cmap="gray")
    ax.set_title('FFT')


    plt.savefig('./img/images_gif_1/exo1_'+str(i)+'.png')
    plt.close()
