import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '',
        component: HomeComponent,
        data: {
          title: 'Home',
        },
      },
      {
        path: 'view-theme',
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
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
