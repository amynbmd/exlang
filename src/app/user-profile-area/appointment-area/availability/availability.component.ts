import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import {MatSlideToggleModule} from '@angular/material/slide-toggle';
import {MatDividerModule} from '@angular/material/divider';
import { FormModule } from 'src/app/_modules/form.module';
import {MatButtonModule} from '@angular/material/button';

@Component({
  selector: 'app-availability',
  templateUrl: './availability.component.html',
  styleUrls: ['./availability.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    MatSlideToggleModule, MatDividerModule, FormModule, MatButtonModule,
  ]
})
export class AvailabilityComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
