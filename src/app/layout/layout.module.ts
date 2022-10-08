import { NgModule } from '@angular/core';
import { MenuComponent } from '../account/menu/menu.component';
import { AppRoutingModule } from '../app-routing.module';
import { SharedModule } from '../_modules/shared.module';
import { ThemeModule } from '../_modules/theme.module';
import { SidebarComponent } from './ui/sidebar/sidebar.component';
import { LayoutComponent } from './layout.component';
import { ThemePickerModule } from './ui/theme-picker/theme-picker';

@NgModule({
  declarations: [LayoutComponent, SidebarComponent, MenuComponent],
  imports: [AppRoutingModule, SharedModule, ThemeModule, ThemePickerModule],
  exports: [LayoutComponent, SidebarComponent, MenuComponent],
})
export class LayoutModule {}
