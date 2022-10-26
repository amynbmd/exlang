import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import {MatCardModule} from '@angular/material/card';
import {MatDividerModule} from '@angular/material/divider';
import {MatIconModule} from '@angular/material/icon';

@Component({
  selector: 'app-upcoming',
  templateUrl: './upcoming.component.html',
  styleUrls: ['./upcoming.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  standalone: true,

  imports: [
    MatCardModule, MatDividerModule, MatIconModule,
  ]
})
export class UpcomingComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
