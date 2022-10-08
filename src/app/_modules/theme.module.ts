import { NgModule } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatMenuModule } from '@angular/material/menu';
import { MatToolbarModule } from '@angular/material/toolbar';

@NgModule({
  exports: [MatButtonModule, MatIconModule, MatMenuModule, MatToolbarModule]
})
export class ThemeModule {}

// No longer used