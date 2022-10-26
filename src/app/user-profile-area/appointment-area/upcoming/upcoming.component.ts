import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatButtonModule} from '@angular/material/button';


@Component({
  selector: 'app-upcoming',
  templateUrl: './upcoming.component.html',
  styleUrls: ['./upcoming.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    MatCardModule, MatDividerModule, MatButtonModule,
  ]
})
export class UpcomingComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
