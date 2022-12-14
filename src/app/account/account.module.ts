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
        path: 'area',
        data: {
          title: 'Account - Registration',
        },
        loadComponent: () => import('./account-area/account-area.component').then(m => m.AccountAreaComponent)
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
