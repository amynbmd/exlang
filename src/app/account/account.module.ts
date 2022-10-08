import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AccountComponent } from './account.component';


const routes: Routes = [
  {
    path: '',
    component: AccountComponent,
    children: [

      {
        path: 'login',
        data: {
          title: 'Account - Login',
        },
        loadComponent: () => import('./login/login.component').then(m => m.LoginComponent)
      },
      {
        path: 'register',
        data: {
          title: 'Account - Registration',
        },
        loadComponent: () => import('./registration/registration.component').then(m => m.RegistrationComponent)
      },
      {
        path: 'register/area',
        data: {
          title: 'Account - Registration',
        },
        loadComponent: () => import('./registration-area/registration-area.component').then(m => m.RegistrationAreaComponent)
      }
    ],
  },
];

@NgModule({
  declarations: [
    AccountComponent,
  ],
  imports: [
    RouterModule.forChild(routes),
  ],
  exports: [],
})
export class AccountModule {}
