import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule, HttpParams } from '@angular/common/http';
import { Component,inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule, HttpClientModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
})
export class LoginComponent {
  
  loginObj: any = {
    "EmailId": "",
    "Password": "",
    "Username": "",
    "ConfirmPassword": ""
  };
  loginObj2: any = {
    "EmailId": "",
    "Password": "",
    "Username": "",
  };
  



  isRegister = false;

  http = inject(HttpClient);

  constructor(private router: Router) {}

  toggleMode(isRegister: boolean) {
    console.log('toggleMode called with isRegister:', isRegister);
    this.isRegister = isRegister;
    this.resetForm();
  }

  resetForm() {
    this.loginObj = {
      "EmailId": "",
      "Password": "",
      "Username": "",
      "ConfirmPassword": ""
    };
  }

  onSubmit() {
    if (this.isRegister) {
      if (this.loginObj.Password !== this.loginObj.ConfirmPassword) {
        // Senhas não coincidem, lógica de tratamento (por exemplo, exibir mensagem de erro)
        alert("As senhas não coincidem");
        return; // Ou outra lógica de tratamento de erro
      } else this.onRegister();
      
    } else {
      this.onLogin();
    }
  }

  onLogin() {
    const params = new HttpParams()
      .set('username', this.loginObj.Username)
      .set('password', this.loginObj.Password);
      
    console.log("aqui esta", params)
    this.http.post<any>("http://localhost/users/login", params.toString(),{
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }).subscribe((res: any) => {
      if (res.access_token) {
        alert("Login Success");
        localStorage.setItem("angular18Login", res.access_token);
        this.router.navigateByUrl("dashboard");
      } else {
        alert("Verifique o nome de usuário ou senha");
      }
    });
  }

  onRegister() {
    this.loginObj2.username = this.loginObj.Username
    this.loginObj2.password = this.loginObj.Password
    this.loginObj2.email = this.loginObj.EmailId

    this.http.post<any>("http://localhost/users", this.loginObj2).subscribe((res: any) => {
      if (res) {
        alert("Registro realizado com sucesso");
        this.toggleMode(false); // Voltar para o modo de login após o registro
      } else {
        alert("Falha no registro");
      }
    });
  }
}
