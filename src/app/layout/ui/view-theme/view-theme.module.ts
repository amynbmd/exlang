import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ViewThemeComponent } from './view-theme.component';
import { SharedModule } from 'src/app/_modules/shared.module';

const routes: Routes = [
  {
    path: '',
    component: ViewThemeComponent,
    data: {
      title: 'View Theme',
    },
  },
];

@NgModule({
  declarations: [ViewThemeComponent],
  imports: [RouterModule.forChild(routes), SharedModule],
  exports: [RouterModule],
})
export class ViewThemeModule {}
