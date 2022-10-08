import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';

@NgModule({
  imports: [CommonModule, MaterialModule, ReactiveFormsModule],
  exports: [CommonModule, MaterialModule, ReactiveFormsModule],
})
export class SharedModule {}
