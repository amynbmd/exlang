import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { RegistrationComponent } from '../registration/registration.component';

@Component({
  selector: 'app-registration-area',
  templateUrl: './registration-area.component.html',
  styleUrls: ['./registration-area.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    RegistrationComponent
  ],
})
export class RegistrationAreaComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
