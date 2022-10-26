import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AuthGuard } from './_shared/AuthGuard.guard';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '',
        component: HomeComponent,
        canActivate: [AuthGuard],
        data: {
          title: 'Home',
        },
      },
      {
        path: 'theme/view',
        loadChildren: () =>
          import('./layout/ui/view-theme/view-theme.module').then(
            (m) => m.ViewThemeModule
          ),
      },
      {
        path: 'account',
        loadChildren: () =>
          import('./account/account.module').then(
            (m) => m.AccountModule
          ),
      },
      {
        path: 'user-profile-area',
        data: {
          title: 'User\'s Profile',
        },
        loadComponent: () => import('./user-profile-area/user-profile-area.component').then(m => m.UserProfileAreaComponent)
      }
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
