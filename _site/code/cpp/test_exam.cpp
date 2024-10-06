#include <iostream>
using namespace std;
class vecteur {
 
public:
vecteur (const int dim_vect,const float* tab) : dim (dim_vect){
  int i;
  elements=new float[dim];
  for (i=0;i<dim;i++)
    elements[i]=tab[i];
}
virtual  ~vecteur(){
  if(dim>0)
    delete [] elements;
}
float operator[](int indice){
  return elements[indice];
}

private:
  float *elements;
  int dim; 
};


int main(){
  float t[10], f;
  vecteur V(10,t) ;
  V[1]=2 ;
  f=V[1];
}
