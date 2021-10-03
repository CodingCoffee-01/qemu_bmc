mkdir build
cd build
../configure
make


//  make arm only 

../configure --target-list=arm-softmmu,arm-linux-user

make -j 8
