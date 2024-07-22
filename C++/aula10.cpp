#include <iostream>
#include <cstdlib>//include necessário para para usar o comando system("cls") , vide linha 12

using namespace std;

int main(){

    int n1,n2,res;
    char opc;

inicio:
    system("cls");

    cout << "Digite o valor da nata 1: ";
    cin >> n1;
    cout << "Digite o valor da nata 2: ";
    cin >> n2;

    res=n1+n2;

    /*
        >=60 Aprovado
        >= 40 e <60 recuperação
        <40 reprovado
    */

    if(res >= 60){
        cout << "\n Aluno aprovado \n";
    }else if(res >=40){
        cout << "\n Aluno em recuperacao \n";
    }else{
        cout << "\n Aluno Reprovado \n";
    }

    cout << "\n Digitar outras notas?(s/n)\n";
    cin >> opc;

    if(opc == 's' or opc == 'S'){
        goto inicio;
    }
	return 0;

}
