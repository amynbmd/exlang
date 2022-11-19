import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CommunityComponent } from './community/community.component';
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
        path: 'account',
        loadChildren: () =>
          import('./account/account.module').then(
            (m) => m.AccountModule
          ),
      },
      {
        path: 'user-profile-area',
        canActivate: [AuthGuard],
        data: {
          title: 'User\'s Profile',
        },
        loadComponent: () => import('./user-profile-area/user-profile-area.component').then(m => m.UserProfileAreaComponent)
      },
      {
        path: 'community',
        component: CommunityComponent,
        canActivate: [AuthGuard],
        data: {
          title: 'Community',
        },
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
