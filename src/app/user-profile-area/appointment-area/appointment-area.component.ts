import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { MatTabsModule } from '@angular/material/tabs';
import { FormModule } from 'src/app/_modules/form.module';
import { AvailabilityComponent } from './availability/availability.component';
import { PastComponent } from './past/past.component';
import { SessionSettingComponent } from './session-setting/session-setting.component';
import { UpcomingComponent } from './upcoming/upcoming.component';

@Component({
  selector: 'app-appointment-area',
  templateUrl: './appointment-area.component.html',
  styleUrls: ['./appointment-area.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,
  imports: [
    MatTabsModule,
    AvailabilityComponent,
    SessionSettingComponent,
    UpcomingComponent,
    PastComponent,
  ]
})
export class AppointmentAreaComponent implements OnInit {
  constructor() {}

  ngOnInit() {}
}
